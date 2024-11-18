import Projects.constants as const

async def repo() -> str:
    return const.REPO_URL

async def live() -> bool:
    return True



