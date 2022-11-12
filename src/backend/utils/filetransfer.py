from fastapi.responses import StreamingResponse
from fastapi import UploadFile
import aiofiles

async def download_file(filename, chunk_size: int=1024 * 1024):
    async def iterfile():
       async with aiofiles.open(filename, 'rb') as f:
            while chunk := await f.read(chunk_size):
                yield chunk
    headers = {'Content-Disposition': f'attachment; filename="{filename.split("/")[-1]}"'}
    return StreamingResponse(iterfile(), headers=headers, media_type='application/x-zip')


async def upload_file(in_file: UploadFile, out_filename, chunk_size: int=1024 * 1024):
    async with aiofiles.open(out_filename, 'wb') as out_file:
        while content := await in_file.read(chunk_size):  # async read chunk
            await out_file.write(content)  # async write chunk

async def upload_db(in_file: UploadFile, out_filename, chunk_size: int=1024 * 1024):
    pass
async def download_db():
    pass