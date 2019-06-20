# monitor_manager
功能1：使用钉钉通知接口，主要分为3个等级
1. info : curl -X POST -s http://127.0.0.1:8000/dingding/info -d "test info"
2. warn : curl -X POST -s http://127.0.0.1:8000/dingding/warn -d "test warn"
3. error: curl -X POST -s http://127.0.0.1:8000/dingding/error -d "test error"


