import asyncio
from pyrogram import Client

api_id = 6
api_hash = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
target_username = "mibombax"

app = Client("my_account", api_id=api_id, api_hash=api_hash)

async def main():
    async with app:
        print(f"شروع اسنایپ برای آیدی @{target_username}...")
        while True:
            try:
                # تلاش برای قفل کردن آیدی روی اکانت شما
                await app.set_username(target_username)
                print(f"🎉 موفقیت! آیدی @{target_username} با موفقیت قفل شد!")
                break
            except Exception as e:
                # خطاهای احتمالی (مثل پر بودن آیدی یا محدودیت) چاپ می‌شود
                print(f"تلاش ناموفق - خطا: {e}")
            
            # فاصله ۲ ثانیه بین هر تلاش
            await asyncio.sleep(2)

app.run(main())
