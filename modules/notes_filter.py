from datetime import datetime

def filter_notes_by_date(notas, fecha_inicio, fecha_fin):
	"""
	Filtra las notas por un rango de fechas (inclusive).
	Las fechas deben estar en formato 'YYYY-MM-DD'.
	"""
	try:
		inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
		fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
	except ValueError:
		print("Formato de fecha inválido. Usa YYYY-MM-DD.")
		return []

	notas_filtradas = []
	for nota in notas:
		try:
			fecha_nota = datetime.strptime(nota["date"][:10], "%Y-%m-%d")
			if inicio <= fecha_nota <= fin:
				notas_filtradas.append(nota)
		except (KeyError, ValueError):
			continue
	return notas_filtradas
