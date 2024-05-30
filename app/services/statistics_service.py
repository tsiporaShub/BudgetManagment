from fastapi.responses import StreamingResponse
import io
import matplotlib.pyplot as plt
from app.services import user_service, operation_service


async def get_users_balance():
    """
    A function that returns a bar graph describing the users' balances
    :return: A picture of the graph
    """
    users = await user_service.get_all_users()
    users_names = []
    users_balance = []
    for u in users:
        users_names.append(u['name'])
        users_balance.append(await operation_service.get_balance(u['id']))

    plt.bar(users_names, users_balance, color='#ff0078')
    plt.title('Users Balance Bar Graph')
    plt.xlabel('Users')
    plt.ylabel('Balance')

    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    plt.close()

    return StreamingResponse(io.BytesIO(img_bytes.read()), media_type="image/png")
