from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/api/v1/detect')
def func(kpi_key: str, timestamp: int, value: float):
    print(type(timestamp), timestamp)
    value = float(value)
    return {'code': 2000, 'message': 'ok', 'data': {
        'kpi_key': kpi_key,
        'timestamp': int(timestamp),
        'value': value,
        'lower': value,
        'upper': value,
        'score': 0, 'anomaly': 0
    }
            }


if __name__ == '__main__':
    uvicorn.run('light_server:app', host='localhost', port=8001)
