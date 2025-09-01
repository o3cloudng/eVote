# eVote System



# Deploy Django on Vercel
1. Setup Databse connection to other DB services (I am using freesql here)
2. Django configurations for Vercel
 

## Create the file in the roo dir build_files.sh
 pip install -r requirements.txt
 python manage.py collectstatic


 ## Create vercel.json
```
{
  "version": 2,
  "builds": [
    {
      "src": "core/wsgi.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "15mb",
        "runtime": "python3.12"
      }
    },
    {
      "src": "build_files.sh",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "staticfiles_build"
      }
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "core/wsgi.py"
    }
  ]
}
```