# Kullanmak istediğiniz temel imajı seçin
FROM node:14

# Çalışma dizinini oluşturun
WORKDIR /app

# Gerekli dosyaları kopyalayın
COPY package*.json ./

# Bağımlılıkları yükleyin
RUN npm install

# Proje dosyalarını kopyalayın
COPY . .

# Docker içinde çalışacak komutu belirtin
CMD ["node", "server.js"]