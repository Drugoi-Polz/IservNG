# Урок_13:

## Работа с SSH:

### Генерация ключа на ПК: 
```bash
ssh-keyhen -t ed25519
```

### Содержимое файла: 
```bash
type .ssh\id_ed25519.pub
```

### Порядок добавления ключа на аккаунт GitHub:
1) Сгенерировать ключ на своём устройстве
2) Скопировать содержимое публичного ключа
3) Добавить ключ в аккаунте GitHub 
```
(settings -> ssh or gpg keys -> add ssh key)
```

## Команды:

### Клонирование репозитория: 
```bash
git clone git@github.com:[username/repositiryname].git
```
### Загрузка обновлений на удалённый репозиторий: 
```bash
git push origin main/master
```
### Загрузка обновлений на локальный репозиторий: 
```bash
git pull origin main/master
```

### Добавить связь с удаленным репозиторием: 
```bash
git remote add origin git@github.com:[username/repositiryname].git
```

