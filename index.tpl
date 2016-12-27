<!DOCTYPE html>
<html>
<head>
    <title>Test tempson</title>
</head>
<body>
    {% if myName == 'jason': %}
    <div>
        <h1>{{ sayHi }}</h1>
    </div>
    {% endif %}
    <div>
        <ul>
            {% for item in list: %}
                {% if not item['name'] == 'C++': %}
                <li>{{ item['name'] }}</li>
                {% endif %}
            {% endfor %}
        </ul>
    </div>
</body>
</html>
