# Destiny Harris
# 04/20/2026
# 5-6 injection

#Incorrect

String username = request.getParameter("username");
String query = "SELECT * FROM users WHERE username = '" + username + "'";
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);

#Fixed

username = request.args.get("username")

query = "SELECT * FROM users WHERE username = %s"
result = db.execute(query, (username,))
