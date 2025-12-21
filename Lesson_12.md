# Работа с Git

### Ссылка на скачивание: https://git-scm.com/install

## Настройка пользователя:

### Имя пользователя: 
```bash
git config --global user.name "[username]"
```

### Почта пользователя: 
```bash
git config --global user.email "[useremail]"
```

## Команды:

### Инициализация репозитория: 
```bash
git init
```
### Проверка состояния репозитория: 
```bash
git status
```
### Добавить файл в комит: 
```bash
git add [file_name]
```

### Добавить все файлы в комит: 
```bash
git add --all
```

### Добавить все файлы текущей директории в комит: 
```bash
git add .
```

### Создание комита с сообщением: 
```bash
git commit -m "[Message]"
```

