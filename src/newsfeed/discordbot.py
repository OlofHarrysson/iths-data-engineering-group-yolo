from discord import SyncWebhook

webhook = SyncWebhook.from_url(
    "https://discord.com/api/webhooks/1131522847509069874/Lwk1yVc4w623xpRPkKYu9faFdMNvV5HTZ3TCcL5DgsIgeqhEvo9tBookvuh2S4IWysTt"
)
webhook.send(
    "Group: iths-data-engineering-group-yolo\nBlog Title: Placeholder for blogtitle\nSummary: Placeholder for summary\nAdditional Info: Placeholder for additional info"
)
