import psycopg2

import config.config as conf


_db_connection = psycopg2.connect(
	"postgresql://{user}:{password}@{host}:{port}/{dbname}".format(
	user=conf.DB_USER,
	password=conf.DB_PASSWORD,
	host=conf.DB_HOST,
	port=conf.DB_PORT,
	dbname=conf.DB_NAME))


def get_dbcon():
	return _db_connection


def select(table: str,  cols: [str], where: {str:any}) -> [{str:any}]:
	con = get_dbcon()
	cur = con.cursor()

	sql = "select " + ",".join(cols)
	sql += " from " + table + " "
	sql += make_sql_where(where) + ";"
	cur.execute(sql)

	return select_results_to_dicts(cols, cur.fetchall())


def insert(table: str, values: {str:any}):
	con = get_dbcon()
	cur = con.cursor()
	keys = values.keys()

	sql = "insert into " + table
	sql += "(" + ",".join(keys)
	sql += ") values(%("
	sql += ")s,%(".join(keys) + ")s);"

	cur.execute(sql, values)
	con.commit()


def update(table: str, values: {str:any}, where: {str:any}):
	con = get_dbcon()
	cur = con.cursor()

	sql = "update " + table
	sql += " set "

	for k in values.keys():
		sql += k + "=%" + k + ")s,"

	sql = sql.rstrip(",") + " "
	sql += make_sql_where(where) + ";"

	cur.execute(sql, values)
	con.commit()


def delete(table: str, where: {str:any}):
	con = get_dbcon()
	cur = con.cursor()

	sql = "delete " + table + " "
	sql += make_sql_where(where) + ";"

	cur.execute(sql)
	con.commit()


def make_sql_where(dic: {str:any}) -> str:
	s = "where "
	for k, v in dic.items():
		if type(v) == str:
			s += k + " = '" + v + "' and "
		else:
			s += k + " = " + str(v) + " and "

	return s.rstrip("and ")


def select_results_to_dicts(cols, results) -> [{str:any}]:
	ls = []
	for item in results:
		d_item = dict(zip(cols, item))
		ls.append(d_item)

	return ls
