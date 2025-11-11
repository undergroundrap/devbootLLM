#!/usr/bin/env python3
"""Add 13 Advanced Django lessons to Python track"""

import json

def load_lessons(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_lessons(path, lessons):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(lessons, f, indent=2, ensure_ascii=False)

def create_django_advanced_lessons():
    """Create 13 comprehensive Advanced Django lessons"""

    lessons = [
        {
            "id": 741,
            "title": "Django Channels - WebSocket Basics",
            "description": "Build real-time applications with Django Channels and WebSockets.",
            "difficulty": "Expert",
            "tags": ["Django", "Channels", "WebSockets", "Real-time", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "# Django Channels WebSocket Consumer\nfrom channels.generic.websocket import WebsocketConsumer\nimport json\n\nclass ChatConsumer(WebsocketConsumer):
    # TODO: Implement connect, disconnect, and receive methods\n    pass\n\nprint(\"ChatConsumer defined\")",
            "fullSolution": "from channels.generic.websocket import WebsocketConsumer\nimport json\n\nclass ChatConsumer(WebsocketConsumer):\n    def connect(self):\n        self.accept()\n    \n    def disconnect(self, close_code):\n        pass\n    \n    def receive(self, text_data):\n        data = json.loads(text_data)\n        message = data['message']\n        self.send(text_data=json.dumps({'message': message}))\n\nprint(\"ChatConsumer defined\")",
            "expectedOutput": "ChatConsumer defined",
            "tutorial": "# Django Channels - WebSocket Basics\n\nDjango Channels extends Django to handle WebSockets, enabling real-time features like chat, notifications, and live updates.\n\n## Why Use Channels?\n\n✓ Real-time bidirectional communication\n✓ Long-lived connections\n✓ Push updates from server to client\n✓ Support for chat, gaming, collaborative apps\n\n## Installation\n\n```bash\npip install channels channels-redis\n```\n\n## Basic Consumer\n\n```python\nfrom channels.generic.websocket import WebsocketConsumer\nimport json\n\nclass ChatConsumer(WebsocketConsumer):\n    def connect(self):\n        # Accept WebSocket connection\n        self.accept()\n    \n    def disconnect(self, close_code):\n        # Clean up when connection closes\n        pass\n    \n    def receive(self, text_data):\n        # Handle messages from WebSocket\n        data = json.loads(text_data)\n        message = data['message']\n        \n        # Echo message back\n        self.send(text_data=json.dumps({\n            'message': message\n        }))\n```\n\n## Routing\n\n```python\n# routing.py\nfrom django.urls import path\nfrom . import consumers\n\nwebsocket_urlpatterns = [\n    path('ws/chat/', consumers.ChatConsumer.as_asgi()),\n]\n```\n\n## Settings Configuration\n\n```python\n# settings.py\nINSTALLED_APPS = [\n    'channels',\n    ...\n]\n\nASGI_APPLICATION = 'myproject.asgi.application'\n\nCHANNEL_LAYERS = {\n    'default': {\n        'BACKEND': 'channels_redis.core.RedisChannelLayer',\n        'CONFIG': {\n            'hosts': [('127.0.0.1', 6379)],\n        },\n    },\n}\n```\n\n## Real-World Example (Slack-like Chat)\n\n```python\nfrom channels.generic.websocket import AsyncWebsocketConsumer\nimport json\n\nclass ChatRoomConsumer(AsyncWebsocketConsumer):\n    async def connect(self):\n        self.room_name = self.scope['url_route']['kwargs']['room_name']\n        self.room_group_name = f'chat_{self.room_name}'\n        \n        # Join room group\n        await self.channel_layer.group_add(\n            self.room_group_name,\n            self.channel_name\n        )\n        await self.accept()\n    \n    async def disconnect(self, close_code):\n        # Leave room group\n        await self.channel_layer.group_discard(\n            self.room_group_name,\n            self.channel_name\n        )\n    \n    async def receive(self, text_data):\n        data = json.loads(text_data)\n        message = data['message']\n        username = data['username']\n        \n        # Send message to room group\n        await self.channel_layer.group_send(\n            self.room_group_name,\n            {\n                'type': 'chat_message',\n                'message': message,\n                'username': username\n            }\n        )\n    \n    async def chat_message(self, event):\n        # Send message to WebSocket\n        await self.send(text_data=json.dumps({\n            'message': event['message'],\n            'username': event['username']\n        }))\n```\n\n## Frontend JavaScript\n\n```javascript\nconst chatSocket = new WebSocket(\n    'ws://' + window.location.host + '/ws/chat/room1/'\n);\n\nchatSocket.onmessage = function(e) {\n    const data = JSON.parse(e.data);\n    console.log('Message:', data.message);\n    // Update UI with message\n};\n\nchatSocket.onclose = function(e) {\n    console.error('Chat socket closed');\n};\n\n// Send message\nfunction sendMessage(message) {\n    chatSocket.send(JSON.stringify({\n        'message': message,\n        'username': 'User123'\n    }));\n}\n```\n\n## Production Deployment\n\n- Use Redis as channel layer backend\n- Deploy with Daphne (ASGI server)\n- Configure nginx to proxy WebSocket connections\n- Scale workers horizontally\n\n## Use Cases\n\n1. **Chat applications** (Slack, Discord)\n2. **Live notifications** (Facebook, Twitter)\n3. **Collaborative editing** (Google Docs)\n4. **Real-time dashboards** (Analytics, monitoring)\n5. **Live sports scores** (ESPN)\n6. **Stock tickers** (Trading platforms)",
            "additionalExamples": "# Example 1: Live Notifications System\nfrom channels.generic.websocket import AsyncWebsocketConsumer\nimport json\n\nclass NotificationConsumer(AsyncWebsocketConsumer):\n    async def connect(self):\n        self.user_id = self.scope['user'].id\n        self.group_name = f'user_{self.user_id}_notifications'\n        \n        await self.channel_layer.group_add(\n            self.group_name,\n            self.channel_name\n        )\n        await self.accept()\n    \n    async def notification(self, event):\n        await self.send(text_data=json.dumps({\n            'type': event['notification_type'],\n            'message': event['message'],\n            'timestamp': event['timestamp']\n        }))\n\n# Send notification from anywhere in Django\nfrom channels.layers import get_channel_layer\nfrom asgiref.sync import async_to_sync\n\ndef send_notification(user_id, message):\n    channel_layer = get_channel_layer()\n    async_to_sync(channel_layer.group_send)(\n        f'user_{user_id}_notifications',\n        {\n            'type': 'notification',\n            'notification_type': 'alert',\n            'message': message,\n            'timestamp': '2024-01-01 12:00:00'\n        }\n    )"
        },
        {
            "id": 742,
            "title": "Django Async Views",
            "description": "Write asynchronous views for improved performance with async/await.",
            "difficulty": "Expert",
            "tags": ["Django", "Async", "Performance", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "# Django async view\nfrom django.http import JsonResponse\nimport asyncio\n\n# TODO: Create async view that fetches data from multiple sources\nasync def dashboard_view(request):\n    # Fetch user data, posts, and notifications concurrently\n    pass\n\nprint(\"Async view defined\")",
            "fullSolution": "from django.http import JsonResponse\nimport asyncio\n\nasync def fetch_user_data():\n    await asyncio.sleep(0.1)\n    return {'name': 'John', 'email': 'john@example.com'}\n\nasync def fetch_posts():\n    await asyncio.sleep(0.1)\n    return [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}]\n\nasync def dashboard_view(request):\n    user_data, posts = await asyncio.gather(\n        fetch_user_data(),\n        fetch_posts()\n    )\n    return JsonResponse({\n        'user': user_data,\n        'posts': posts\n    })\n\nprint(\"Async view defined\")",
            "expectedOutput": "Async view defined",
            "tutorial": "# Django Async Views\n\nDjango 3.1+ supports async views, allowing you to write high-performance async/await code for I/O-bound operations.\n\n## Why Async Views?\n\n✓ Better performance for I/O-bound operations\n✓ Handle more concurrent requests\n✓ Non-blocking database queries\n✓ Efficient API calls and external service requests\n\n## Basic Async View\n\n```python\nfrom django.http import JsonResponse\nimport httpx\n\nasync def async_view(request):\n    async with httpx.AsyncClient() as client:\n        response = await client.get('https://api.example.com/data')\n    return JsonResponse(response.json())\n```\n\n## Concurrent Operations\n\n```python\nimport asyncio\nfrom django.http import JsonResponse\n\nasync def fetch_user(user_id):\n    # Simulated async database query\n    await asyncio.sleep(0.1)\n    return {'id': user_id, 'name': 'John'}\n\nasync def fetch_posts(user_id):\n    await asyncio.sleep(0.1)\n    return [{'id': 1, 'title': 'Post 1'}]\n\nasync def fetch_friends(user_id):\n    await asyncio.sleep(0.1)\n    return [{'id': 2, 'name': 'Jane'}]\n\nasync def dashboard(request, user_id):\n    # Run all three queries concurrently\n    user, posts, friends = await asyncio.gather(\n        fetch_user(user_id),\n        fetch_posts(user_id),\n        fetch_friends(user_id)\n    )\n    \n    return JsonResponse({\n        'user': user,\n        'posts': posts,\n        'friends': friends\n    })\n```\n\n## Async ORM (Django 4.1+)\n\n```python\nfrom django.http import JsonResponse\nfrom myapp.models import Article\n\nasync def article_list(request):\n    # Async database query\n    articles = [article async for article in Article.objects.all()]\n    \n    return JsonResponse({\n        'articles': [\n            {'id': a.id, 'title': a.title}\n            for a in articles\n        ]\n    })\n\nasync def article_detail(request, pk):\n    # Async get\n    article = await Article.objects.aget(pk=pk)\n    \n    return JsonResponse({\n        'id': article.id,\n        'title': article.title,\n        'content': article.content\n    })\n```\n\n## Real-World Example (Aggregating APIs)\n\n```python\nimport httpx\nimport asyncio\nfrom django.http import JsonResponse\nfrom django.views import View\n\nclass AggregatedDataView(View):\n    async def get(self, request):\n        async with httpx.AsyncClient() as client:\n            # Fetch from multiple APIs concurrently\n            weather_task = client.get('https://api.weather.com/current')\n            news_task = client.get('https://api.news.com/top')\n            stocks_task = client.get('https://api.stocks.com/quotes')\n            \n            responses = await asyncio.gather(\n                weather_task,\n                news_task,\n                stocks_task,\n                return_exceptions=True\n            )\n            \n            # Handle results\n            weather = responses[0].json() if not isinstance(responses[0], Exception) else None\n            news = responses[1].json() if not isinstance(responses[1], Exception) else None\n            stocks = responses[2].json() if not isinstance(responses[2], Exception) else None\n            \n            return JsonResponse({\n                'weather': weather,\n                'news': news,\n                'stocks': stocks\n            })\n```\n\n## Performance Comparison\n\n```python\n# Sync view (slow - sequential)\ndef sync_dashboard(request):\n    user = fetch_user()      # 100ms\n    posts = fetch_posts()    # 100ms\n    friends = fetch_friends() # 100ms\n    # Total: 300ms\n    return JsonResponse({...})\n\n# Async view (fast - concurrent)\nasync def async_dashboard(request):\n    user, posts, friends = await asyncio.gather(\n        fetch_user(),\n        fetch_posts(),\n        fetch_friends()\n    )\n    # Total: ~100ms (3x faster!)\n    return JsonResponse({...})\n```\n\n## When to Use Async Views\n\n✓ **Use async when**:\n- Making multiple API calls\n- Heavy I/O operations\n- Real-time features\n- WebSocket handling\n\n✗ **Don't use async for**:\n- CPU-bound operations\n- Simple CRUD operations\n- When ORM doesn't support async",
            "additionalExamples": "# Example 1: Multi-Service Data Aggregation\nimport httpx\nimport asyncio\nfrom django.http import JsonResponse\n\nasync def get_user_profile(request, username):\n    async with httpx.AsyncClient(timeout=5.0) as client:\n        # Fetch from multiple microservices\n        profile_task = client.get(f'http://profile-service/users/{username}')\n        activity_task = client.get(f'http://activity-service/users/{username}/recent')\n        badges_task = client.get(f'http://gamification-service/users/{username}/badges')\n        \n        try:\n            profile_resp, activity_resp, badges_resp = await asyncio.gather(\n                profile_task,\n                activity_task,\n                badges_task\n            )\n            \n            return JsonResponse({\n                'profile': profile_resp.json(),\n                'recent_activity': activity_resp.json(),\n                'badges': badges_resp.json()\n            })\n        except Exception as e:\n            return JsonResponse({'error': str(e)}, status=500)\n\nprint(\"Multi-service aggregation view defined\")"
        }
    ]

    # Add remaining 11 lessons
    lessons.extend([
        {
            "id": 743,
            "title": "GraphQL with Graphene-Django",
            "description": "Build GraphQL APIs in Django using Graphene library.",
            "difficulty": "Expert",
            "tags": ["Django", "GraphQL", "Graphene", "API", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "# GraphQL schema with Graphene\nimport graphene\n\nclass Query(graphene.ObjectType):\n    # TODO: Define hello query that returns greeting\n    pass\n\nschema = graphene.Schema(query=Query)\nresult = schema.execute('{ hello }')\nprint(result.data)",
            "fullSolution": "import graphene\n\nclass Query(graphene.ObjectType):\n    hello = graphene.String(name=graphene.String(default_value=\"World\"))\n    \n    def resolve_hello(self, info, name):\n        return f\"Hello {name}!\"\n\nschema = graphene.Schema(query=Query)\nresult = schema.execute('{ hello }')\nprint(result.data)",
            "expectedOutput": "{'hello': 'Hello World!'}",
            "tutorial": "# GraphQL with Graphene-Django\n\nGraphQL provides a flexible alternative to REST APIs, allowing clients to request exactly the data they need.\n\n## Basic Schema\n\n```python\nimport graphene\nfrom graphene_django import DjangoObjectType\n\nclass UserType(DjangoObjectType):\n    class Meta:\n        model = User\n        fields = ('id', 'username', 'email')\n\nclass Query(graphene.ObjectType):\n    users = graphene.List(UserType)\n    user = graphene.Field(UserType, id=graphene.Int())\n    \n    def resolve_users(self, info):\n        return User.objects.all()\n    \n    def resolve_user(self, info, id):\n        return User.objects.get(pk=id)\n\nschema = graphene.Schema(query=Query)\n```\n\n## Mutations\n\n```python\nclass CreateUser(graphene.Mutation):\n    class Arguments:\n        username = graphene.String(required=True)\n        email = graphene.String(required=True)\n    \n    user = graphene.Field(UserType)\n    \n    def mutate(self, info, username, email):\n        user = User.objects.create(username=username, email=email)\n        return CreateUser(user=user)\n\nclass Mutation(graphene.ObjectType):\n    create_user = CreateUser.Field()\n\nschema = graphene.Schema(query=Query, mutation=Mutation)\n```",
            "additionalExamples": "# Example: GitHub-style GraphQL API\nimport graphene\n\nclass Repository(graphene.ObjectType):\n    name = graphene.String()\n    stars = graphene.Int()\n    \nclass Query(graphene.ObjectType):\n    repository = graphene.Field(Repository, name=graphene.String())\n    \n    def resolve_repository(self, info, name):\n        return Repository(name=name, stars=1234)\n\nschema = graphene.Schema(query=Query)\nresult = schema.execute('{ repository(name: \"django\") { name stars } }')\nprint(result.data)"
        },
        {
            "id": 744,
            "title": "Django Custom Middleware",
            "description": "Create custom middleware for request/response processing.",
            "difficulty": "Expert",
            "tags": ["Django", "Middleware", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "# Custom logging middleware\nclass RequestLoggingMiddleware:\n    def __init__(self, get_response):\n        self.get_response = get_response\n    \n    def __call__(self, request):\n        # TODO: Log request method and path before processing\n        response = self.get_response(request)\n        # TODO: Log response status after processing\n        return response\n\nprint(\"Middleware defined\")",
            "fullSolution": "class RequestLoggingMiddleware:\n    def __init__(self, get_response):\n        self.get_response = get_response\n    \n    def __call__(self, request):\n        print(f\"Request: {request.method} {request.path}\")\n        response = self.get_response(request)\n        print(f\"Response: {response.status_code}\")\n        return response\n\nprint(\"Middleware defined\")",
            "expectedOutput": "Middleware defined",
            "tutorial": "# Django Custom Middleware\n\nMiddleware processes every request/response, enabling features like authentication, logging, and rate limiting.\n\n## Middleware Structure\n\n```python\nclass MyMiddleware:\n    def __init__(self, get_response):\n        self.get_response = get_response\n        # One-time initialization\n    \n    def __call__(self, request):\n        # Code executed before view\n        response = self.get_response(request)\n        # Code executed after view\n        return response\n```\n\n## Common Use Cases\n\n```python\n# Rate limiting middleware\nfrom django.core.cache import cache\nfrom django.http import HttpResponseTooManyRequests\n\nclass RateLimitMiddleware:\n    def __init__(self, get_response):\n        self.get_response = get_response\n    \n    def __call__(self, request):\n        ip = request.META['REMOTE_ADDR']\n        key = f'ratelimit_{ip}'\n        requests = cache.get(key, 0)\n        \n        if requests >= 100:  # 100 requests per minute\n            return HttpResponseTooManyRequests(\"Rate limit exceeded\")\n        \n        cache.set(key, requests + 1, 60)\n        return self.get_response(request)\n```",
            "additionalExamples": "# Example: Request timing middleware\nimport time\n\nclass TimingMiddleware:\n    def __init__(self, get_response):\n        self.get_response = get_response\n    \n    def __call__(self, request):\n        start = time.time()\n        response = self.get_response(request)\n        duration = time.time() - start\n        response['X-Request-Duration'] = f\"{duration:.2f}s\"\n        return response"
        },
        {
            "id": 745,
            "title": "Django Signals",
            "description": "Use signals for decoupled event-driven programming in Django.",
            "difficulty": "Expert",
            "tags": ["Django", "Signals", "Events", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "# Django signals\nfrom django.db.models.signals import post_save\nfrom django.dispatch import receiver\n\n# TODO: Create signal receiver that prints when User is saved\n\nprint(\"Signal receiver defined\")",
            "fullSolution": "from django.db.models.signals import post_save\nfrom django.dispatch import receiver\n\nclass User:\n    def __init__(self, username):\n        self.username = username\n\n@receiver(post_save, sender=User)\ndef user_saved(sender, instance, created, **kwargs):\n    action = 'created' if created else 'updated'\n    print(f\"User {instance.username} was {action}\")\n\nprint(\"Signal receiver defined\")",
            "expectedOutput": "Signal receiver defined",
            "tutorial": "# Django Signals\n\nSignals allow decoupled applications to get notified when certain actions occur.\n\n## Built-in Signals\n\n- `pre_save` / `post_save`: Before/after model save\n- `pre_delete` / `post_delete`: Before/after model delete\n- `m2m_changed`: Many-to-many relations change\n\n## Basic Usage\n\n```python\nfrom django.db.models.signals import post_save\nfrom django.dispatch import receiver\nfrom django.contrib.auth.models import User\n\n@receiver(post_save, sender=User)\ndef create_user_profile(sender, instance, created, **kwargs):\n    if created:\n        Profile.objects.create(user=instance)\n```\n\n## Custom Signals\n\n```python\nfrom django.dispatch import Signal\n\n# Define custom signal\norder_placed = Signal()\n\n# Send signal\norder_placed.send(sender=Order, order_id=123, amount=99.99)\n\n# Receive signal\n@receiver(order_placed)\ndef send_confirmation_email(sender, order_id, amount, **kwargs):\n    send_email(f\"Order {order_id} confirmed: ${amount}\")\n```",
            "additionalExamples": "# Example: Audit logging with signals\nfrom django.db.models.signals import post_save, post_delete\n\n@receiver(post_save)\ndef log_save(sender, instance, created, **kwargs):\n    action = 'created' if created else 'updated'\n    print(f\"AuditLog: {sender.__name__} {instance.pk} {action}\")\n\n@receiver(post_delete)\ndef log_delete(sender, instance, **kwargs):\n    print(f\"AuditLog: {sender.__name__} {instance.pk} deleted\")"
        },
        {
            "id": 746,
            "title": "Custom Management Commands",
            "description": "Create custom Django management commands for CLI operations.",
            "difficulty": "Expert",
            "tags": ["Django", "CLI", "Management Commands", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "# Custom management command\nfrom django.core.management.base import BaseCommand\n\nclass Command(BaseCommand):\n    help = 'Export users to CSV'\n    \n    # TODO: Implement handle method\n    def handle(self, *args, **options):\n        pass\n\nprint(\"Command class defined\")",
            "fullSolution": "from django.core.management.base import BaseCommand\n\nclass Command(BaseCommand):\n    help = 'Export users to CSV'\n    \n    def add_arguments(self, parser):\n        parser.add_argument('--limit', type=int, default=100)\n    \n    def handle(self, *args, **options):\n        limit = options['limit']\n        self.stdout.write(f\"Exporting {limit} users...\")\n        self.stdout.write(self.style.SUCCESS('Export complete'))\n\nprint(\"Command class defined\")",
            "expectedOutput": "Command class defined",
            "tutorial": "# Custom Management Commands\n\nManagement commands extend Django's manage.py with custom CLI tools.\n\n## Structure\n\n```python\n# myapp/management/commands/my_command.py\nfrom django.core.management.base import BaseCommand\n\nclass Command(BaseCommand):\n    help = 'Description of command'\n    \n    def add_arguments(self, parser):\n        parser.add_argument('--option', type=str)\n    \n    def handle(self, *args, **options):\n        self.stdout.write('Executing...')\n        self.stdout.write(self.style.SUCCESS('Done!'))\n```\n\n## Usage\n\n```bash\npython manage.py my_command --option value\n```\n\n## Real Examples\n\n```python\nclass Command(BaseCommand):\n    help = 'Clean old sessions'\n    \n    def add_arguments(self, parser):\n        parser.add_argument('--days', type=int, default=30)\n    \n    def handle(self, *args, **options):\n        cutoff = timezone.now() - timedelta(days=options['days'])\n        count = Session.objects.filter(expire_date__lt=cutoff).delete()[0]\n        self.stdout.write(f\"Deleted {count} sessions\")\n```",
            "additionalExamples": "# Example: Data import command\nclass Command(BaseCommand):\n    help = 'Import products from CSV'\n    \n    def add_arguments(self, parser):\n        parser.add_argument('file', type=str)\n    \n    def handle(self, *args, **options):\n        import csv\n        with open(options['file']) as f:\n            reader = csv.DictReader(f)\n            for row in reader:\n                Product.objects.create(**row)\n        self.stdout.write(self.style.SUCCESS('Import complete'))"
        },
        {
            "id": 747,
            "title": "Background Tasks with Celery",
            "description": "Integrate Celery for asynchronous task processing in Django.",
            "difficulty": "Expert",
            "tags": ["Django", "Celery", "Background Tasks", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "# Celery task\nfrom celery import shared_task\n\n# TODO: Create task that sends email asynchronously\n@shared_task\ndef send_email_task(to, subject, body):\n    pass\n\nprint(\"Celery task defined\")",
            "fullSolution": "from celery import shared_task\nimport time\n\n@shared_task\ndef send_email_task(to, subject, body):\n    time.sleep(0.1)  # Simulate email sending\n    return f\"Email sent to {to}: {subject}\"\n\nprint(\"Celery task defined\")",
            "expectedOutput": "Celery task defined",
            "tutorial": "# Background Tasks with Celery\n\nCelery handles asynchronous tasks outside the request/response cycle.\n\n## Setup\n\n```python\n# celery.py\nfrom celery import Celery\n\napp = Celery('myproject')\napp.config_from_object('django.conf:settings', namespace='CELERY')\napp.autodiscover_tasks()\n```\n\n## Creating Tasks\n\n```python\nfrom celery import shared_task\n\n@shared_task\ndef send_welcome_email(user_id):\n    user = User.objects.get(pk=user_id)\n    send_email(user.email, 'Welcome!')\n    return f\"Email sent to {user.email}\"\n```\n\n## Calling Tasks\n\n```python\n# Async (returns immediately)\nresult = send_welcome_email.delay(user_id=123)\n\n# Schedule for later\nsend_welcome_email.apply_async(args=[123], countdown=3600)\n\n# Check result\nif result.ready():\n    print(result.get())\n```\n\n## Periodic Tasks\n\n```python\nfrom celery.schedules import crontab\n\n@app.task\ndef cleanup_old_data():\n    Session.objects.filter(expired=True).delete()\n\napp.conf.beat_schedule = {\n    'cleanup-every-night': {\n        'task': 'myapp.tasks.cleanup_old_data',\n        'schedule': crontab(hour=2, minute=0)\n    }\n}\n```",
            "additionalExamples": "# Example: Report generation\n@shared_task\ndef generate_sales_report(month, year):\n    orders = Order.objects.filter(date__month=month, date__year=year)\n    total = sum(o.amount for o in orders)\n    report = f\"Sales Report {month}/{year}: ${total}\"\n    # Save to S3, send email, etc.\n    return report"
        }
    ])

    # Add final 7 lessons (IDs 748-754)
    lessons.extend([
        {
            "id": 748,
            "title": "DRF Custom Permissions",
            "description": "Implement custom permission classes in Django REST Framework.",
            "difficulty": "Expert",
            "tags": ["Django", "DRF", "Permissions", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "from rest_framework import permissions\n\n# TODO: Create permission that allows only owners to edit\nclass IsOwnerOrReadOnly(permissions.BasePermission):\n    pass\n\nprint(\"Permission class defined\")",
            "fullSolution": "from rest_framework import permissions\n\nclass IsOwnerOrReadOnly(permissions.BasePermission):\n    def has_object_permission(self, request, view, obj):\n        if request.method in permissions.SAFE_METHODS:\n            return True\n        return obj.owner == request.user\n\nprint(\"Permission class defined\")",
            "expectedOutput": "Permission class defined",
            "tutorial": "# DRF Custom Permissions\n\nPermissions control who can perform which actions on resources.\n\n## Basic Permission\n\n```python\nfrom rest_framework import permissions\n\nclass IsOwner(permissions.BasePermission):\n    def has_object_permission(self, request, view, obj):\n        return obj.owner == request.user\n```\n\n## Using in Views\n\n```python\nfrom rest_framework import viewsets\n\nclass ArticleViewSet(viewsets.ModelViewSet):\n    queryset = Article.objects.all()\n    permission_classes = [IsOwnerOrReadOnly]\n```",
            "additionalExamples": "# Example: Role-based permission\nclass IsPremiumUser(permissions.BasePermission):\n    message = 'Upgrade to premium to access this feature'\n    \n    def has_permission(self, request, view):\n        return request.user.is_authenticated and request.user.is_premium"
        },
        {
            "id": 749,
            "title": "DRF Pagination Strategies",
            "description": "Implement different pagination styles in Django REST Framework.",
            "difficulty": "Expert",
            "tags": ["Django", "DRF", "Pagination", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "from rest_framework.pagination import PageNumberPagination\n\n# TODO: Create custom pagination class with page_size=10\nclass CustomPagination(PageNumberPagination):\n    pass\n\nprint(\"Pagination class defined\")",
            "fullSolution": "from rest_framework.pagination import PageNumberPagination\n\nclass CustomPagination(PageNumberPagination):\n    page_size = 10\n    page_size_query_param = 'page_size'\n    max_page_size = 100\n\nprint(\"Pagination class defined\")",
            "expectedOutput": "Pagination class defined",
            "tutorial": "# DRF Pagination\n\n## Page Number Pagination\n\n```python\nclass StandardPagination(PageNumberPagination):\n    page_size = 20\n    page_size_query_param = 'size'\n    max_page_size = 100\n```\n\n## Cursor Pagination\n\n```python\nfrom rest_framework.pagination import CursorPagination\n\nclass TimestampPagination(CursorPagination):\n    page_size = 50\n    ordering = '-created_at'\n```\n\n## Limit-Offset Pagination\n\n```python\nclass LimitOffsetPagination(LimitOffsetPagination):\n    default_limit = 25\n    max_limit = 100\n```",
            "additionalExamples": "# Example: Custom response format\nclass CustomPageNumberPagination(PageNumberPagination):\n    def get_paginated_response(self, data):\n        return Response({\n            'total_pages': self.page.paginator.num_pages,\n            'current_page': self.page.number,\n            'results': data\n        })"
        },
        {
            "id": 750,
            "title": "API Throttling and Rate Limiting",
            "description": "Implement rate limiting to protect API endpoints.",
            "difficulty": "Expert",
            "tags": ["Django", "DRF", "Throttling", "Rate Limiting", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "from rest_framework.throttling import UserRateThrottle\n\n# TODO: Create throttle class limiting to 100 requests/hour\nclass BurstRateThrottle(UserRateThrottle):\n    pass\n\nprint(\"Throttle class defined\")",
            "fullSolution": "from rest_framework.throttling import UserRateThrottle\n\nclass BurstRateThrottle(UserRateThrottle):\n    rate = '100/hour'\n\nprint(\"Throttle class defined\")",
            "expectedOutput": "Throttle class defined",
            "tutorial": "# API Throttling\n\n## Built-in Throttles\n\n```python\nfrom rest_framework.throttling import AnonRateThrottle, UserRateThrottle\n\nclass AnonThrottle(AnonRateThrottle):\n    rate = '10/hour'  # Anonymous users\n\nclass UserThrottle(UserRateThrottle):\n    rate = '1000/day'  # Authenticated users\n```\n\n## Apply to Views\n\n```python\nclass ArticleViewSet(viewsets.ModelViewSet):\n    throttle_classes = [AnonThrottle, UserThrottle]\n```",
            "additionalExamples": "# Example: Custom scope throttle\nclass PremiumUserThrottle(UserRateThrottle):\n    scope = 'premium'\n    \n    def allow_request(self, request, view):\n        if request.user.is_premium:\n            self.rate = '10000/day'\n        else:\n            self.rate = '100/day'\n        return super().allow_request(request, view)"
        },
        {
            "id": 751,
            "title": "API Versioning Strategies",
            "description": "Implement API versioning for backward compatibility.",
            "difficulty": "Expert",
            "tags": ["Django", "DRF", "Versioning", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "from rest_framework.versioning import URLPathVersioning\n\n# TODO: Create versioning class for URL path versioning\nclass APIVersioning(URLPathVersioning):\n    pass\n\nprint(\"Versioning class defined\")",
            "fullSolution": "from rest_framework.versioning import URLPathVersioning\n\nclass APIVersioning(URLPathVersioning):\n    default_version = 'v1'\n    allowed_versions = ['v1', 'v2']\n\nprint(\"Versioning class defined\")",
            "expectedOutput": "Versioning class defined",
            "tutorial": "# API Versioning\n\n## URL Path Versioning\n\n```python\n# urls.py\npath('api/v1/users/', UserListView.as_view())\npath('api/v2/users/', UserListViewV2.as_view())\n```\n\n## Header Versioning\n\n```python\nfrom rest_framework.versioning import AcceptHeaderVersioning\n\nclass MyAcceptHeaderVersioning(AcceptHeaderVersioning):\n    allowed_versions = ['1.0', '2.0']\n```\n\n## Version-Specific Logic\n\n```python\nclass UserSerializer(serializers.ModelSerializer):\n    def to_representation(self, instance):\n        data = super().to_representation(instance)\n        if self.context['request'].version == 'v2':\n            data['full_name'] = f\"{instance.first_name} {instance.last_name}\"\n        return data\n```",
            "additionalExamples": "# Example: Namespace versioning\nfrom rest_framework.versioning import NamespaceVersioning\n\nclass MyNamespaceVersioning(NamespaceVersioning):\n    default_version = 'v1'\n    allowed_versions = ['v1', 'v2', 'v3']"
        },
        {
            "id": 752,
            "title": "CORS Configuration",
            "description": "Configure Cross-Origin Resource Sharing for API access.",
            "difficulty": "Expert",
            "tags": ["Django", "CORS", "Security", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "# CORS configuration\n# TODO: Configure CORS settings for production\nCORS_ALLOWED_ORIGINS = []\nCORS_ALLOW_CREDENTIALS = False\n\nprint(\"CORS configured\")",
            "fullSolution": "CORS_ALLOWED_ORIGINS = [\n    'https://example.com',\n    'https://app.example.com'\n]\nCORS_ALLOW_CREDENTIALS = True\nCORS_ALLOW_METHODS = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']\n\nprint(\"CORS configured\")",
            "expectedOutput": "CORS configured",
            "tutorial": "# CORS Configuration\n\n## Installation\n\n```bash\npip install django-cors-headers\n```\n\n## Settings\n\n```python\nINSTALLED_APPS = [\n    'corsheaders',\n    ...\n]\n\nMIDDLEWARE = [\n    'corsheaders.middleware.CorsMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    ...\n]\n\nCORS_ALLOWED_ORIGINS = [\n    'https://example.com',\n    'https://www.example.com',\n]\n\nCORS_ALLOW_CREDENTIALS = True\n```\n\n## Development\n\n```python\nCORS_ALLOW_ALL_ORIGINS = True  # Development only!\n```",
            "additionalExamples": "# Example: Custom CORS logic\nCORS_ALLOWED_ORIGIN_REGEXES = [\n    r'^https://\\w+\\.example\\.com$',\n]\nCORS_ALLOW_HEADERS = [\n    'accept',\n    'authorization',\n    'content-type',\n    'x-api-key',\n]"
        },
        {
            "id": 753,
            "title": "Django Testing Strategies",
            "description": "Write comprehensive tests for Django applications.",
            "difficulty": "Expert",
            "tags": ["Django", "Testing", "pytest", "Expert"],
            "category": "Web Development",
            "language": "python",
            "baseCode": "from django.test import TestCase, Client\n\n# TODO: Create test class for User model\nclass UserModelTest(TestCase):\n    def setUp(self):\n        pass\n    \n    def test_user_creation(self):\n        pass\n\nprint(\"Test class defined\")",
            "fullSolution": "from django.test import TestCase, Client\n\nclass User:\n    def __init__(self, username, email):\n        self.username = username\n        self.email = email\n\nclass UserModelTest(TestCase):\n    def setUp(self):\n        self.user = User(username='testuser', email='test@example.com')\n    \n    def test_user_creation(self):\n        self.assertEqual(self.user.username, 'testuser')\n        self.assertEqual(self.user.email, 'test@example.com')\n\nprint(\"Test class defined\")",
            "expectedOutput": "Test class defined",
            "tutorial": "# Django Testing Strategies\n\n## Unit Tests\n\n```python\nfrom django.test import TestCase\n\nclass UserModelTest(TestCase):\n    def setUp(self):\n        self.user = User.objects.create(username='test')\n    \n    def test_user_str(self):\n        self.assertEqual(str(self.user), 'test')\n```\n\n## Integration Tests\n\n```python\nfrom django.test import Client\n\nclass ViewTest(TestCase):\n    def test_homepage(self):\n        client = Client()\n        response = client.get('/')\n        self.assertEqual(response.status_code, 200)\n```\n\n## API Tests\n\n```python\nfrom rest_framework.test import APITestCase\n\nclass APITest(APITestCase):\n    def test_create_user(self):\n        response = self.client.post('/api/users/', {'username': 'test'})\n        self.assertEqual(response.status_code, 201)\n```",
            "additionalExamples": "# Example: pytest with fixtures\nimport pytest\n\n@pytest.fixture\ndef api_client():\n    from rest_framework.test import APIClient\n    return APIClient()\n\n@pytest.mark.django_db\ndef test_user_list(api_client):\n    response = api_client.get('/api/users/')\n    assert response.status_code == 200"
        }
    ])

    return lessons

# Load existing lessons
print("Loading existing Python lessons...")
lessons = load_lessons('public/lessons-python.json')
print(f"Current count: {len(lessons)} lessons")

# Create Django Advanced lessons
print("\nCreating 13 Advanced Django lessons...")
django_lessons = create_django_advanced_lessons()
print(f"Created {len(django_lessons)} Django Advanced lessons")

# Add to end temporarily (will reorganize later)
next_id = max(lesson['id'] for lesson in lessons) + 1
for lesson in django_lessons:
    lesson['id'] = next_id
    next_id += 1

lessons.extend(django_lessons)

# Save
print(f"\nSaving {len(lessons)} total lessons...")
save_lessons('public/lessons-python.json', lessons)

print("\nAdvanced Django lessons added successfully!")
print(f"New lesson IDs: {django_lessons[0]['id']}-{django_lessons[-1]['id']}")
