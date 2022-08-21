import core.db as db  


def signup(username: str, password: str):
	db.insert("users", { 
		"user_name": username,
		"password": password
	})

def select_by_username(username: str) -> [{str:any}]:
	return db.select(
		"users", 
		["user_id", "user_name", "password"], 
		{"user_name": username}
	)













	
