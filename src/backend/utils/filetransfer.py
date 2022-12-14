from pathlib import Path
from fastapi.responses import StreamingResponse
from fastapi import UploadFile
import aiofiles

async def download_file(filename: Path, media_type: str='octet-stream', chunk_size: int=1024 * 1024):
    try:
        filename = Path(filename)
    except:
        raise ValueError('Invalid filename')
    async def iterfile():
        async with aiofiles.open(filename, 'rb') as f:
            while chunk := await f.read(chunk_size):
                yield chunk
    headers = {'Content-Disposition': f'attachment; filename="{filename.name}"'}
    return StreamingResponse(iterfile(), headers=headers, media_type=media_type)


async def upload_file(in_file: UploadFile, out_filename, chunk_size: int=1024 * 1024):
    async with aiofiles.open(out_filename, 'wb') as out_file:
        while content := await in_file.read(chunk_size):  # async read chunk
            await out_file.write(content)  # async write chunk

async def upload_db(in_file: UploadFile, out_filename, chunk_size: int=1024 * 1024):
    pass
async def download_db():
    pass