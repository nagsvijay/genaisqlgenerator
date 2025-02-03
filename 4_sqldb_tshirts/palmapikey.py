import google.generativeai as palm

palm.configure(api_key="AIzaSyAnZ3nhAcJqhWJjh3rWaApM5SOQiA9k-4o")

try:
    models = palm.list_models()
    print(models)
except Exception as e:
    print("API Key issue:", e)


from google.generativeai import configure, list_models

configure(api_key="AIzaSyAnZ3nhAcJqhWJjh3rWaApM5SOQiA9k-4o")

try:
    models = list_models()
    print("Available models:", [model.name for model in models])
except Exception as e:
    print("Error:", e)
