from datetime import datetime

birth = datetime.strptime(
    input("Please enter your date of birth in the format YYYY-MM-DD: "), "%Y-%m-%d"
)
today = datetime.today()

diff = int((today - birth).days)
years = diff // 365

print(years)
