from Penyimpanan.Database.Instagram import Main

class Freestyle:
  def __init__(self) -> None:
    pass

  def ZoraaDev(self):
    try: Main().Pengecekan_Data()
    except (Exception) as e: exit(e)


Freestyle().ZoraaDev()
