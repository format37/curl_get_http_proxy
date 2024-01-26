# Build with name telegram_proxy
# sudo docker build -t telegram_proxy .

# Build with name telegram_proxy
# sudo docker build -t --force-rm telegram_proxy .
# Build with name telegram_proxy force rebuild and recreate
sudo docker build --no-cache --force-rm -t telegram_proxy .
# Run as a daemon
# sudo docker run -d telegram_proxy
# Run as a daemon with 5000 port
sudo docker run -d -p 5000:5000 telegram_proxy