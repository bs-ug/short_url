# Skracacz URLi

Z długiego URLa robi krótkiego i odwrotnie.

## Uruchamianie

### Standardowo
`python manage.py runserver`

### Dockerowo
- budowanie kontenera: `docker-compose build`
- uruchamianie aplikacji: `docker-compose up -d`
- zamykanie aplikacji: `docker-compose down`

## Używanie
`http://localhost:8000/api/url`

### Metody
- `GET /api/url` - zwraca listę przetworzonych URLi w krótkiej i długiej wersji,
- `GET /api/url?short=<str>` - zwraca długą wersję URLa dla krótkiego podanego w parametrze `short`,
- `POST /api/url` - tworzy krótką wersję URLa dla długiej wysłanej w `body` zapytania.

### `body` metody POST
 ```
 {
   "long": <str>
 }
```