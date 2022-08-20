import core.db as db  


def signup(username: str, password: str):
	db.insert("user", { 
		"user_name": username,
		"password": password
	})

def select_by_username(username: str) -> [{str:any}]:
	return db.select(
		"user", 
		["user_id", "user_name", "password"], 
		{"user_name": username}
	)













	
