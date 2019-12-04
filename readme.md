# 提交

git add . & git commit -m fixed

# Url

传参 <book_id>
path include

# urls

命名空间
使用 app_name

# include

include(module,namespace=None)

```python
urlpatterns=[
    path('book/',include('book.urls','book'))
]
```

include((pattern_list,app_namespace),namespace=None)
include(pattern_list)

```C#
int main(){
    return 0;
}
```

# re

r"" 代表原生字符串 (raw) 不转义
r'\n'

# Django Template Language
