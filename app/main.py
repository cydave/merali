import dataclasses
from dataclasses import dataclass
import multiprocessing
from fastapi import FastAPI, Request, Response
from fastapi.responses import PlainTextResponse, JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from app.logger import logger


limiter = Limiter(key_func=get_remote_address, headers_enabled=True)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@dataclass
class RateLimit:
    limit: int
    remaining: int
    reset: int


def get_ratelimit_stats(request: Request):
    current_limit = request.state.view_rate_limit
    window_stats = limiter.limiter.get_window_stats(current_limit[0], *current_limit[1])
    return RateLimit(
        limit=current_limit[0].amount,
        remaining=window_stats[1],
        reset=1 + window_stats[0],
    )


@app.get("/")
async def index(request: Request):
    logger.info("[pid:%d] Serving /index", multiprocessing.current_process().pid)
    return PlainTextResponse("You've reached the index.")


@app.get("/limited", response_class=JSONResponse)
@limiter.limit("5/hour")
async def ratelimited(request: Request, response: Response):
    pid = multiprocessing.current_process().pid
    logger.info("[pid:%d] Serving /ratelimited", pid)
    get_ratelimit_stats(request)
    stats = get_ratelimit_stats(request)
    return {"pid": pid, "rate_limit": dataclasses.asdict(stats)}


@app.get("/reset")
async def reset(request: Request):
    logger.info("[pid:%d] Serving /reset", multiprocessing.current_process().pid)
    return PlainTextResponse("Rate limit reset.")
