## Django + Vue.js

Reference: https://developer.aliyun.com/article/932995  

## Command line history

```bash
mkdir django-vuejs
cd django-vuejs

conda create -n django311 python=3.11
conda activate django311

conda install django

django-admin startproject django_vuejs

cd django_vuejs
python manage.py migrate
python manage.py startapp api

vim django_vuejs/settings.py

vim api/models.py
vim api/views.py
vim api/urls.py

vim django_vuejs/urls.py

python manage.py makemigrations api
python manage.py migrate

sqlite3 -cmd ".mode column" -cmd ".headers on" db.sqlite3
SELECT name FROM sqlite_master WHERE type='table';
PRAGMA table_info(table_name);
SELECT * FROM api_book;
.quit
```

```bash
nvm use node
npm install -g @vue/cli
npm install -g @vue/cli-init

vue init webpack frontend

cd frontend
npm install
npm install vue-resource
npm install element-ui

cd src/components
vim Home.vue

cd ..
cd router
vim index.js

cd ..
vim main.js

conda install conda-forge::django-cors-headers
cd ../..
vim django_vuejs/settings.py

cd frontend
vim config/index.js
npm run dev

npm run build
vim django_vuejs/urls.py
vim django_vuejs/settings.py
python manage.py runserver 0.0.0.0:9080
```
