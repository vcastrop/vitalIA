from vitalIA_app.models import Medicamento, StockMedicamento

# Obtener todos los medicamentos
medicamentos = Medicamento.objects.all()

if not medicamentos.exists():
    print("❌ No hay medicamentos en la base de datos.")
else:
    print("\n📋 LISTADO DE MEDICAMENTOS DISPONIBLES\n" + "="*40)

    for medicamento in medicamentos:
        print(f"\n✅ Medicamento: {medicamento.nombre}")
        print(f"📜 Descripción: {medicamento.descripcion if medicamento.descripcion else 'No disponible'}")

        # Obtener los precios y stock del medicamento en distintas farmacias
        stock_medicamentos = StockMedicamento.objects.filter(medicamento=medicamento).order_by('precio')

        if not stock_medicamentos.exists():
            print("💰 Precio: No disponible")
            print("📦 Stock: No disponible")
        else:
            print("💰 Precios y farmacias:")
            for stock in stock_medicamentos:
                print(f"   🏪 {stock.farmacia.nombre} - ${stock.precio} - 📦 Stock: {stock.stock}")

    print("\n🔍 Fin del listado\n")
