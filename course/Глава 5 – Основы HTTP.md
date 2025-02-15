[HTTP](<https://github.com/abadd00d/web-for-juniors/blob/main/HTTP.md>) (HyperText Transfer Protocol) — это протокол, который обеспечивает взаимодействие между клиентом (например, веб-браузером) и сервером по модели «клиент-сервер». Клиент отправляет HTTP-запрос на сервер, а сервер обрабатывает его и возвращает HTTP-ответ.

![Pasted image 20250215171426.png](<https://github.com/abadd00d/web-for-juniors/blob/main/img/Pasted image 20250215171426.png>)

Основные моменты:
1. Взаимодействие по HTTP подразумевает запрос от клиента и ответ на этот запрос от сервера. Есть ситуации, когда ответа нет: таймаут соединения и другие проблемы – их пока не касаемся.
2. Каждый отет имеет статус-код. Есть всего пять групп кодов: 1хх, 2хх, 3xx, 4xx, 5xx. Например код 200 означает успешное выполнение запроса.
3. В HTTP речь идет об обьектах, а не о файлах. Даже если ты запрашиваешь image.jpg, то корректнее говорить, что запрашивается обьект image.jpg.
4. Ключевая характеристика объекта – [URI](<https://github.com/abadd00d/web-for-juniors/blob/main/URI.md>). Запрос к обьекту идет по определенному URI.
5. В запросе и ответе всегда (в 99.99999% случаев) присутствуют хоть какие-то заголовки. Заголовки несут дополнительную информацию, которая помогает обрабатывать запрос или ответ.
6. В запросе также могут присутствовать [аргументы запроса](<https://github.com/abadd00d/web-for-juniors/blob/main/аргументы запроса.md>).
7. Запрос может использовать разный  HTTP-метод. На этом этапе нам нужно знать только GET, POST и HEAD. Есть и другие, о них позже или читай сам.

## Пример взаимодействия клиент-сервер

**Запрос от клиента**
Клиент формирует HTTP-запрос, который состоит из:
- **Строки запроса**: содержит метод (например, `GET`, `POST`), URI (адрес ресурса) и версию протокола (например, `HTTP/1.1`).
- **Заголовков**: метаданные, которые описывают запрос (например, `Host`, `User-Agent`, `Accept`).
- **Тела запроса** (опционально): данные, передаваемые на сервер (например, при отправке формы через `POST`).
Пример запроса:
```
    GET /index.html HTTP/1.1
    Host: example.com
    User-Agent: Mozilla/5.0
    Accept: text/html
```

**Ответ от сервера**
Сервер обрабатывает запрос и возвращает HTTP-ответ, который включает:
- **Строку статуса**: содержит версию протокола, статус-код и пояснение (например, `HTTP/1.1 200 OK`).
- **Заголовки**: метаданные, описывающие ответ (например, `Content-Type`, `Content-Length`).  
- **Тело ответа** (опционально): запрошенные данные (например, HTML-страница).

Пример ответа:
```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1234

<html>...</html>
```

## Отправляем наш первый запрос

В предыдущей главе тебе уже удалось открыть страницу. По сути ты сделал несколько запросов с помощью браузера. Давай теперь выполним запрос руками в консоли. Можешь сдать его с той же машины, где у тебя хостится твой сайт, но я рекоменую иметь локальную машину для выполнения команд.

Открывай терминал и запускай:

```
curl https://hello.cdn.ngenix.net/
```

> Про утилиту [curl](<https://github.com/abadd00d/web-for-juniors/blob/main/curl.md>) читай [тут](<https://github.com/abadd00d/web-for-juniors/blob/main/тут.md>).

В ответ ты получишь примерно следующее:

```
<!DOCTYPE html>
<html>
  <head>
    <link href="styles.css" rel="stylesheet">
    <meta charset="utf-8">
    <title>NGENIX Test Page</title>
  </head>
  <body>
    <div class="head">Тестовая страница</div>
    <div class="logo"><img src="/ngenix_logo.png" alt="NGENIX" height="200px"></div>
</body>
</html>
```

Т.е. все отлично, мы получили HTML-код. Можешь заменить команду и попробовать тоже самое со своим сайтом, запущенным в прошлой главе:

```
curl http://IP_адрес_твоей_VPS/
```

Обрати внимание, что схема запроса изменена на  http. Т.к. у тебя еще не настроена работа по https, то и пытаться сделать запрос по нему бессмысленно.

### Смотрим код ответа и заголовки

Пулучить ответ – полдела. Очень часто важная информация передается передается в заголовках. Кроме этого обязательно нужно контролировать код-ответа – это поможет тебе понять, что произошло.

Для этого будем использовать опцию `-v` : она делает вывод команды более подробным.


```
curl -v https://hello.cdn.ngenix.net/
```

Получаем:

```
* Host hello.cdn.ngenix.net:443 was resolved.
* IPv6: (none)
* IPv4: 93.93.91.146
*   Trying 93.93.91.146:443...
* Connected to hello.cdn.ngenix.net (93.93.91.146) port 443
* ALPN: curl offers h2,http/1.1
* (304) (OUT), TLS handshake, Client hello (1):
*  CAfile: /etc/ssl/cert.pem
*  CApath: none
* (304) (IN), TLS handshake, Server hello (2):
* (304) (IN), TLS handshake, Unknown (8):
* (304) (IN), TLS handshake, Certificate (11):
* (304) (IN), TLS handshake, CERT verify (15):
* (304) (IN), TLS handshake, Finished (20):
* (304) (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / AEAD-AES256-GCM-SHA384 / [blank] / UNDEF
* ALPN: server accepted h2
* Server certificate:
*  subject: CN=*.cdn.ngenix.net
*  start date: Apr  3 16:02:01 2024 GMT
*  expire date: May  5 12:24:27 2025 GMT
*  subjectAltName: host "hello.cdn.ngenix.net" matched cert's "*.cdn.ngenix.net"
*  issuer: C=BE; O=GlobalSign nv-sa; CN=GlobalSign GCC R3 DV TLS CA 2020
*  SSL certificate verify ok.
* using HTTP/2
* [HTTP/2] [1] OPENED stream for https://hello.cdn.ngenix.net/
* [HTTP/2] [1] [:method: GET]
* [HTTP/2] [1] [:scheme: https]
* [HTTP/2] [1] [:authority: hello.cdn.ngenix.net]
* [HTTP/2] [1] [:path: /]
* [HTTP/2] [1] [user-agent: curl/8.7.1]
* [HTTP/2] [1] [accept: */*]
> GET / HTTP/2
> Host: hello.cdn.ngenix.net
> User-Agent: curl/8.7.1
> Accept: */*
>
* Request completely sent off
< HTTP/2 200
< server: nginx
< date: Sat, 15 Feb 2025 14:16:23 GMT
< content-type: text/html
< content-length: 323
< last-modified: Fri, 28 Jun 2024 10:43:48 GMT
< etag: "7d5137a9a8542f37b70902cd29bf70cf"
< x-amz-request-id: tx00000000000005daf9b5c-006697c38b-68194524-default
< x-ngenix-storage: ADC
< x-ngenix-cache: HIT
< accept-ranges: bytes
<
<!DOCTYPE html>
<html>
  <head>
    <link href="styles.css" rel="stylesheet">
    <meta charset="utf-8">
    <title>NGENIX Test Page</title>
  </head>
  <body>
    <div class="head">Тестовая страница</div>
    <div class="logo"><img src="/ngenix_logo.png" alt="NGENIX" height="200px"></div>
</body>
</html>
* Connection #0 to host hello.cdn.ngenix.net left intact
```

Да, тут много всего. Но нас пока интересуют два вида строк: те, которые начинаются с символа `>` (заголовки запроса) и те, которые начинаются с символа `<` (заголовки ответа). Также имейте в виду, что в конце вывода идет тело ответа, где HTML-теги также начинаются на символ  `<` – это не заголовки, а. именно тело ответа, важно это помнить.

Важно помнить, что формат выглядит следующим образом:
`Заголовок: значение`

Например:
`Host: hello.cdn.ngenix.net`
или
`User-Agent: curl/8.7.1`
и т.п.
### Несколько важных заголовков

Заголовки запроса:
- Host – тут передается значение домена, к которому идет обращение. Важно в современном вебе, т.к. на одном адресе может располагаться множество веб-ресурсов и именно по этому заголовку веб-сервер поймет, какому сайту принадлежит запрос.
- User-Agent – тут передается значение вашего агента – программы, которой вы делаете запрос. Для браузера будет что-то типа `Mozilla/5.0 (platform; rv:gecko-version) Gecko/gecko-trail Firefox/firefox-version` .
- Accept – показывает, какой тип контента мы подразумеваем получить и какой сможем распознать.

Заголовки ответа:
- server – какой сервер отдал ответ.
- date – дата, когда ответ был сформирован.
- content-type – в какойм формате передан контент, важно для его интерпретации на клиенте.
- content-length – количество переданных байт тела запроса.
- last-modified – дата последнего изменения контента.

### Код ответа

Один из самых важных параметров ответа сервера. В нашем случае он равен 200, что означает, что ответ был успешно обработан.

```
...
< HTTP/2 200
...
```

# Итого

Мы научились отправлять запрос "руками" через консоль.

# Задание

1. Сделать запросы к другим сайтам, попробовать проанализировать заголовки.

# Материалы
- Заголовки и их описание подробно – https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers
- Статусы – https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- Методы – https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods


➡️ К следующей главе "[Глава 5 – Основы HTTP](<https://github.com/abadd00d/web-for-juniors/blob/main/Глава 5 – Основы HTTP.md>)