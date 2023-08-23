from discord import SyncWebhook

group = "iths-data-engineering-group-yolo"
title = "Placeholder for blogtitle"
summary = "Placeholder for summary"
info = "Placeholder for additional info"

webhook = SyncWebhook.from_url(
    "https://discord.com/api/webhooks/1131522847509069874/Lwk1yVc4w623xpRPkKYu9faFdMNvV5HTZ3TCcL5DgsIgeqhEvo9tBookvuh2S4IWysTt"
)
webhook.send(f"Group: {group}\nBlog Title: {title}\nSummary: {summary}\nAdditional Info: {info}")
