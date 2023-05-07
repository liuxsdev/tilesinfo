FROM python:slim

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

CMD ["uvicorn","main:app","--host","0.0.0.0"]