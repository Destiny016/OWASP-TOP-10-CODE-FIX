# Destiny Harris
# 04-20-2026
# Correction description

# Broken Access Control
- The endpoints allow any authenticated or unauthenticated users to access any users data by changing the userId

- The fix works because it enforces object level authentication, and ensures users can only access their own data.

# Cryptographic Failures
- No salt means it's vulnerable to rainbow table attacks

- The fix works because it includes salt automatically, and resistant to brute force attacks

# Injections
- User input is directly concatenated into the SQL query

- The fix prevents query manipulation and enforces strict typing and parameterization.

# Insecure Design
- No indentity verification
- No authentication
- weak password handeling 

- The fix uses secure token based flow, and confirms ownership before reset.

# Software and Data Integrity Failure
- No integrity Verification
- Supply chain risk
- No protection

- The fix uses subresource integrity and prevents loading altered scripts

# Server Side Request Forgery
- Full user control of outbound requests
- Can access internal systems
- data exposure

- The fix restricts outbound requests and prevents internal network access. 
