BASE_URL = http://localhost:8000/
TOKEN = "Your token"

curl --data "token=$TOKEN&amount=$1&text=$2" $BASE_URL/submit/income/

