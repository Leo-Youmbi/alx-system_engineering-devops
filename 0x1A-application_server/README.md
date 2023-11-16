# 0x1A Application server :wrench:

> Using a shell script is most useful for repetitive tasks that may be time consuming to execute by typing one line at a time. A few examples of applications shell scripts can be used for include: Automating the code compiling process. Running a program or creating a program environment. This project covers deploying the application server in  real environemnt.

At the end of this project, I was able to solve these questions:

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231116%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231116T114712Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=b1aad8694fd089b98bceac8288842edefed867a76318b331c71b09e29193af20)

## Tasks :heavy_check_mark:

0. Nginx config file to serve a page from the route /airbnb-onepage/
1. Nginx config file by adding another service for Gunicorn to handle. In AirBnB_clone_v2/web_flask/6-number_odd_or_even, the route /number_odd_or_even/<int:n>
2. Nginx config file must serve a page both locally and on its public IP on port 80


## Results :chart_with_upwards_trend:

| Filename |
| ------ |
| [2-app_server-nginx_config](./2-app_server-nginx_config)|
| [3-app_server-nginx_config](./3-app_server-nginx_config)|
| [4-app_server-nginx_config](./4-app_server-nginx_config)|
| [5-app_server-nginx_config](./5-app_server-nginx_config)|
| [4-reload_gunicorn_no_downtime](./4-reload_gunicorn_no_downtime)|
| [gunicorn.service](./gunicorn.service)|


## Additional info :construction:
### Resources

- emacs
- BASH
- Debian 9 stable / Ubuntu 16.04 / Ubuntu 18.04 
- Shellcheck
- Gunicorn
- Nginx


### Try It On Your Machine :computer:
```bash
git clone https://github.com/Leo-Youmbi/alx-system_engineering-devops.git
NO TESTS FOR THIS PROJECT :)

```
