from rest_framework import serializers
from .models import Customer, Seller, Product, Sale, SaleProduct


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    commission_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = "__all__"

    def get_commission_percentage(self, obj):
        return obj.calculate_product_commission_percentage()


class SaleProductSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="product.id", read_only=True)
    code = serializers.CharField(source="product.code", read_only=True)
    description = serializers.CharField(source="product.description", read_only=True)
    price = serializers.DecimalField(
        source="product.price", max_digits=10, decimal_places=2, read_only=True
    )
    commission_percentage = serializers.SerializerMethodField()
    commission = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = SaleProduct
        fields = [
            "id",
            "code",
            "description",
            "quantity",
            "price",
            "commission_percentage",
            "commission",
            "total_price",
        ]

    def get_total_price(self, obj):
        return obj.calculate_total_price()

    def get_commission_percentage(self, obj):
        return obj.product.calculate_product_commission_percentage()

    def get_commission(self, obj):
        return obj.calculate_product_commission()


class SaleSerializer(serializers.ModelSerializer):
    total_value = serializers.SerializerMethodField()
    quantity_of_items = serializers.SerializerMethodField()
    total_commission = serializers.SerializerMethodField()
    products = SaleProductSerializer(many=True, source="saleproduct_set")

    class Meta:
        model = Sale
        fields = "__all__"
        depth = 1

    def get_total_value(self, obj):
        return obj.calculate_sale_total_value()

    def get_quantity_of_items(self, obj):
        return obj.count_items()

    def get_total_commission(self, obj):
        return obj.calculate_total_commission()


class SaleProductCreateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField()
    quantity = serializers.IntegerField()

    class Meta:
        model = SaleProduct
        fields = ["id", "quantity"]


class SaleCreateSerializer(serializers.ModelSerializer):
    products = SaleProductCreateSerializer(many=True, write_only=True)

    class Meta:
        model = Sale
        fields = ["date", "customer", "seller", "products"]

    def create(self, validated_data):
        products = validated_data.pop("products", [])

        if not products:
            raise serializers.ValidationError("Sale must have at least one product.")

        sale = Sale.objects.create(**validated_data)

        for product_data in products:
            product = Product.objects.get(id=product_data["id"])
            quantity = product_data["quantity"]
            SaleProduct.objects.create(sale=sale, product=product, quantity=quantity)
        return sale


class SaleUpdateSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ["date", "customer", "seller", "products"]

    def update(self, instance, validated_data):
        if not instance.products.exists():
            raise serializers.ValidationError("Sale must have at least one product.")
        return super().update(instance, validated_data)
