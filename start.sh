if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/henockjoy/AsunaReload.git /AsunaReload
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /AsunaReload
fi
cd /AsunaReload
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
