# E-commerce-backend
An e-commerce app .

for register the user
path: url/auth/register/
json format
{
    "first_name": "naman",
    "last_name":"garg",
    "phone_no": 8860433367,
    "address":"shiv ram park",
    "email":"namangarg820@gmail.com",
    "password":"naman12911"
}

for login the user

path: url/auth/login/

json format:
{
    "email":"namangarg820@gmail.com",
    "password":"naman12911"
}

for logout:
path : url/auth/logout/

json:
{ "refresh": "token"
}
