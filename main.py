import asyncio
from pyrogram import Client
from pyrogram.errors import FloodWait, UsernameOccupied

api_id = 6
api_hash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

# اون متن طولانی که توی کولب کپی کردی رو دقیقاً بین دو تا دابل کوتیشن (" ") پایین بچسبون:
SESSION_STRING = "BAAAAAYATMQ53OdZYK1UeCJBa2Jzu8pHBvvIJ1lxdmUFZLJVTq843vkwCzzGXqh5UWv67_43YjeSGI0tqaHy9_BH1lCH4pwirv4zwWkKUH-n3-QxXU3AZtM9CTin6fnYshdPRhqdOhp-6jOfYrv6H0mgXX-31eRP9OttnqQUext3Rs3aL8fmtFtcOnZENobrhdo2zCMj7JJnShii7BjdSiYqFxgy6KFDge-HyvTYxIwPYeRLady6D8HETD5LMIgK5wrSiE4nXeOQt-tBQSUa3wdypl1G57bggoLxvCysyZGB3r1e7Y65ZiqmWyUn6A32dd7cdiTButNjGXAEoscsqCcW14YLrAAAAAHbaQvyA"

chat_id = -1004449203929  # آیدی عددی کانال شما
target_username = "mimbobaxko"  # آیدی که می‌خواهید اسنایپ کنید

app = Client("my_account", api_id=api_id, api_hash=api_hash, session_string=SESSION_STRING)

async def main():
    async with app:
        print(f"شروع اسنایپ برای آیدی @{target_username} روی کانال...")
        while True:
            try:
                # تلاش برای قفل کردن آیدی روی کانال
                await app.set_chat_username(chat_id, target_username)
                print(f"🎉 موفقیت بزرگ! آیدی @{target_username} با موفقیت روی کانال قفل شد!")
                break
            except UsernameOccupied:
                print("آیدی هنوز توسط شخص دیگری گرفته شده است...")
            except FloodWait as e:
                print(f"محدودیت تلگرام! صبر به مدت {e.value} ثانیه...")
                await asyncio.sleep(e.value)
            except Exception as e:
                print(f"خطا: {e}")
            
            # فاصله ۱.۵ ثانیه بین هر تلاش برای جلوگیری از محدودیت
            await asyncio.sleep(1.5)

app.run(main())
