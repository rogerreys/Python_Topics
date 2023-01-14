import requests as req

def get_catalog():
    r = req.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text, type(r.text), end="---"*50)
    categories = r.json()
    category = [cate['name'] for cate in categories]
    print(category)
    #return r

if __name__ == '__main__':
    get_catalog()