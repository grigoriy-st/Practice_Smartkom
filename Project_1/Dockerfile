# Используем официальный образ Nginx
FROM nginx:alpine

# Удаляем дефолтный конфиг Nginx (если нужна кастомная конфигурация)
# RUN rm /etc/nginx/conf.d/default.conf

# Копируем ваш конфиг (если есть)
COPY nginx/default.conf /etc/nginx/conf.d/

# Копируем HTML-файлы в контейнер
COPY index.html /usr/share/nginx/html/
