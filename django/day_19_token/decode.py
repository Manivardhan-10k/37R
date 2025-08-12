import jwt 

try:
 decoded=jwt.decode('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoia2FseWFuIiwiYmF0Y2giOiIzNyIsImlzX2FkbWluIjpmYWxzZSwiZXhwIjoxNzU0ODg3Mzg5LCJpYXQiOjE3NTQ4ODczODR9.S3WrHsE2BGHHezJ4n4iaC_Pqy5pfz6nUYz7ys26i2js','hello from python',algorithms=["HS256"])
except Exception as e:
    print(e)