from django.db import models
from django.conf import settings

class Note(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, #このモデルがどのユーザーモデルと紐づくかを指定
        on_delete=models.CASCADE, #ユーザーが削除されたら、その人のノートも一緒に削除される
        related_name='notes',     #userからnotes一覧を引く時の逆引き名
        null=True, blank=True,   # 既存公開ノートを生かすため一時的に許可
    )
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
