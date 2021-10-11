from django.db import models

# Create your models here.


class SizingOrder(models.Model):
    date = models.DateField(default=datetime.datetime.now())
    title = models.CharField(blank=True, max_length=150)
    productdesc = models.CharField(blank=True, max_length=150)
    timestamp = models.DateField(auto_now_add=True)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    value_base = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount_base = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_value_base = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    is_paid = models.BooleanField(default=True)
    objects = models.Manager()
    browser = SizingOrderManager()

    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs):
        sizingorder_items: object = self.sizingorder_items.all()
        self.value = sizingorder_items.aggregate(Sum('total_price'))['total_price__sum'] if sizingorder_items.exists() else 0.00
        self.final_value = Decimal(self.value) - Decimal(self.discount)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'New SizingOrder'

    def get_edit_url(self):
        return reverse('update_sizingorder', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('delete_sizingorder', kwargs={'pk': self.id})

    def tag_final_value(self):
        return f'{self.final_value} '

    def tag_discount(self):
        return f'{self.discount}'

    def tag_value(self):
        return f'{self.value}'

    def tag_final_value_base(self):
        return f'{self.final_value_base}'

    def tag_discount_base(self):
        return f'{self.discount_base}'

    def tag_value_base(self):
        return f'{self.value_base}'

    @staticmethod
    def filter_data(request, queryset):
        search_name = request.GET.get('search_name', None)
        date_start = request.GET.get('date_start', None)
        date_end = request.GET.get('date_end', None)
        queryset = queryset.filter(title__contains=search_name) if search_name else queryset
        if date_end and date_start and date_end >= date_start:
            date_start = datetime.datetime.strptime(date_start, '%m/%d/%Y').strftime('%Y-%m-%d')
            date_end = datetime.datetime.strptime(date_end, '%m/%d/%Y').strftime('%Y-%m-%d')
            print(date_start, date_end)
            queryset = queryset.filter(date__range=[date_start, date_end])
        return queryset


class SizingOrderItem(models.Model):
    avproduct = models.ForeignKey(Avproduct, on_delete=models.PROTECT)
    sizingorder = models.ForeignKey(SizingOrder, on_delete=models.CASCADE, related_name='sizingorder_items')
    qty = models.PositiveIntegerField(default=1)
    addlconsole = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    total_price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)

    base = models.FloatField(default='0')
    discount_base = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_base = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    total_base = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)

    fte = models.FloatField(default='0')
    discount_fte = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    final_fte = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    total_fte = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)

    productcomplexityfac = models.FloatField(default='1.0')
    numworkstation = models.IntegerField(default='0')
    numserver = models.IntegerField(db_column='Numserver', default='0')
    numipaddress = models.IntegerField(default='0')
    total_endpoints = models.IntegerField(default='0')
    desc = models.CharField(blank=True, max_length=150)

    numappchange = models.IntegerField(default='0')

    SrvsHoursCalc = models.FloatField(default='0')
    WkstnsHoursCalc = models.FloatField(default='0')
    IPsHoursCalc = models.FloatField(default='0')
    AddlConHoursCalc = models.FloatField(default='0')
    AppChangeHoursCalc = models.FloatField(default='0')

    AppChangeFac = models.FloatField(default='0')
    ServerFTE = models.FloatField(default='0')
    WorkstationFTE = models.FloatField(default='0')
    IPEndpointFTE = models.FloatField(default='0')
    AddlConFTE = models.FloatField(default='0')

    DefaultFTE_Year = models.FloatField(default='0')
    NumMonths_1 = models.IntegerField(default='0')
    DeliveryCtrCostFactor = models.FloatField(default='0')

    # Component #1
    ProdComponent1_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent1_Wkstn = models.BooleanField(default=False)
    ProdComponent1_WkstnHours = models.FloatField(default='0')
    ProdComponent1_Svr = models.BooleanField(default=False)
    ProdComponent1_SvrHours = models.FloatField(default='0')
    ProdComponent1_IP = models.BooleanField(default=False)
    ProdComponent1_IPHours = models.FloatField(default='0')
    ProdComponent1_Ttl_Hours = models.FloatField(default='0')
    ProdComponent1_Ttl_FTE = models.FloatField(default='0')

    # Component #2
    ProdComponent2_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent2_Wkstn = models.BooleanField(default=False)
    ProdComponent2_WkstnHours = models.FloatField(default='0')
    ProdComponent2_Svr = models.BooleanField(default=False)
    ProdComponent2_SvrHours = models.FloatField(default='0')
    ProdComponent2_IP = models.BooleanField(default=False)
    ProdComponent2_IPHours = models.FloatField(default='0')
    ProdComponent2_Ttl_Hours = models.FloatField(default='0')
    ProdComponent2_Ttl_FTE = models.FloatField(default='0')

    # Component #3
    ProdComponent3_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent3_Wkstn = models.BooleanField(default=False)
    ProdComponent3_WkstnHours = models.FloatField(default='0')
    ProdComponent3_Svr = models.BooleanField(default=False)
    ProdComponent3_SvrHours = models.FloatField(default='0')
    ProdComponent3_IP = models.BooleanField(default=False)
    ProdComponent3_IPHours = models.FloatField(default='0')
    ProdComponent3_Ttl_Hours = models.FloatField(default='0')
    ProdComponent3_Ttl_FTE = models.FloatField(default='0')

    # Component #4
    ProdComponent4_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent4_Wkstn = models.BooleanField(default=False)
    ProdComponent4_WkstnHours = models.FloatField(default='0')
    ProdComponent4_Svr = models.BooleanField(default=False)
    ProdComponent4_SvrHours = models.FloatField(default='0')
    ProdComponent4_IP = models.BooleanField(default=False)
    ProdComponent4_IPHours = models.FloatField(default='0')
    ProdComponent4_Ttl_Hours = models.FloatField(default='0')
    ProdComponent4_Ttl_FTE = models.FloatField(default='0')

    # Component #5
    ProdComponent5_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent5_Wkstn = models.BooleanField(default=False)
    ProdComponent5_WkstnHours = models.FloatField(default='0')
    ProdComponent5_Svr = models.BooleanField(default=False)
    ProdComponent5_SvrHours = models.FloatField(default='0')
    ProdComponent5_IP = models.BooleanField(default=False)
    ProdComponent5_IPHours = models.FloatField(default='0')
    ProdComponent5_Ttl_Hours = models.FloatField(default='0')
    ProdComponent5_Ttl_FTE = models.FloatField(default='0')

    # Component #6
    ProdComponent6_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent6_Wkstn = models.BooleanField(default=False)
    ProdComponent6_WkstnHours = models.FloatField(default='0')
    ProdComponent6_Svr = models.BooleanField(default=False)
    ProdComponent6_SvrHours = models.FloatField(default='0')
    ProdComponent6_IP = models.BooleanField(default=False)
    ProdComponent6_IPHours = models.FloatField(default='0')
    ProdComponent6_Ttl_Hours = models.FloatField(default='0')
    ProdComponent6_Ttl_FTE = models.FloatField(default='0')

    # Component #7
    ProdComponent7_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent7_Wkstn = models.BooleanField(default=False)
    ProdComponent7_WkstnHours = models.FloatField(default='0')
    ProdComponent7_Svr = models.BooleanField(default=False)
    ProdComponent7_SvrHours = models.FloatField(default='0')
    ProdComponent7_IP = models.BooleanField(default=False)
    ProdComponent7_IPHours = models.FloatField(default='0')
    ProdComponent7_Ttl_Hours = models.FloatField(default='0')
    ProdComponent7_Ttl_FTE = models.FloatField(default='0')

    # Component #8
    ProdComponent8_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent8_Wkstn = models.BooleanField(default=False)
    ProdComponent8_WkstnHours = models.FloatField(default='0')
    ProdComponent8_Svr = models.BooleanField(default=False)
    ProdComponent8_SvrHours = models.FloatField(default='0')
    ProdComponent8_IP = models.BooleanField(default=False)
    ProdComponent8_IPHours = models.FloatField(default='0')
    ProdComponent8_Ttl_Hours = models.FloatField(default='0')
    ProdComponent8_Ttl_FTE = models.FloatField(default='0')

    # Component #9
    ProdComponent9_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent9_Wkstn = models.BooleanField(default=False)
    ProdComponent9_WkstnHours = models.FloatField(default='0')
    ProdComponent9_Svr = models.BooleanField(default=False)
    ProdComponent9_SvrHours = models.FloatField(default='0')
    ProdComponent9_IP = models.BooleanField(default=False)
    ProdComponent9_IPHours = models.FloatField(default='0')
    ProdComponent9_Ttl_Hours = models.FloatField(default='0')
    ProdComponent9_Ttl_FTE = models.FloatField(default='0')

    # Component #10
    ProdComponent10_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent10_Wkstn = models.BooleanField(default=False)
    ProdComponent10_WkstnHours = models.FloatField(default='0')
    ProdComponent10_Svr = models.BooleanField(default=False)
    ProdComponent10_SvrHours = models.FloatField(default='0')
    ProdComponent10_IP = models.BooleanField(default=False)
    ProdComponent10_IPHours = models.FloatField(default='0')
    ProdComponent10_Ttl_Hours = models.FloatField(default='0')
    ProdComponent10_Ttl_FTE = models.FloatField(default='0')

    # Component #11
    ProdComponent11_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent11_Wkstn = models.BooleanField(default=False)
    ProdComponent11_WkstnHours = models.FloatField(default='0')
    ProdComponent11_Svr = models.BooleanField(default=False)
    ProdComponent11_SvrHours = models.FloatField(default='0')
    ProdComponent11_IP = models.BooleanField(default=False)
    ProdComponent11_IPHours = models.FloatField(default='0')
    ProdComponent11_Ttl_Hours = models.FloatField(default='0')
    ProdComponent11_Ttl_FTE = models.FloatField(default='0')

    # Component #12
    ProdComponent12_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent12_Wkstn = models.BooleanField(default=False)
    ProdComponent12_WkstnHours = models.FloatField(default='0')
    ProdComponent12_Svr = models.BooleanField(default=False)
    ProdComponent12_SvrHours = models.FloatField(default='0')
    ProdComponent12_IP = models.BooleanField(default=False)
    ProdComponent12_IPHours = models.FloatField(default='0')
    ProdComponent12_Ttl_Hours = models.FloatField(default='0')
    ProdComponent12_Ttl_FTE = models.FloatField(default='0')

    # Component #13
    ProdComponent13_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent13_Wkstn = models.BooleanField(default=False)
    ProdComponent13_WkstnHours = models.FloatField(default='0')
    ProdComponent13_Svr = models.BooleanField(default=False)
    ProdComponent13_SvrHours = models.FloatField(default='0')
    ProdComponent13_IP = models.BooleanField(default=False)
    ProdComponent13_IPHours = models.FloatField(default='0')
    ProdComponent13_Ttl_Hours = models.FloatField(default='0')
    ProdComponent13_Ttl_FTE = models.FloatField(default='0')

    # Component #14
    ProdComponent14_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent14_Wkstn = models.BooleanField(default=False)
    ProdComponent14_WkstnHours = models.FloatField(default='0')
    ProdComponent14_Svr = models.BooleanField(default=False)
    ProdComponent14_SvrHours = models.FloatField(default='0')
    ProdComponent14_IP = models.BooleanField(default=False)
    ProdComponent14_IPHours = models.FloatField(default='0')
    ProdComponent14_Ttl_Hours = models.FloatField(default='0')
    ProdComponent14_Ttl_FTE = models.FloatField(default='0')

    # Component #15
    ProdComponent15_Desc = models.CharField(blank=True, max_length=150)
    ProdComponent15_Wkstn = models.BooleanField(default=False)
    ProdComponent15_WkstnHours = models.FloatField(default='0')
    ProdComponent15_Svr = models.BooleanField(default=False)
    ProdComponent15_SvrHours = models.FloatField(default='0')
    ProdComponent15_IP = models.BooleanField(default=False)
    ProdComponent15_IPHours = models.FloatField(default='0')
    ProdComponent15_Ttl_Hours = models.FloatField(default='0')
    ProdComponent15_Ttl_FTE = models.FloatField(default='0')


    SoftLifeSvrYesNo = models.BooleanField(default=False)
    SoftLifeSrvHoursCalc = models.FloatField(default='0')
    SoftLifeSvrFTE = models.FloatField(default='0')



    def __str__(self):
        return f'{self.avproduct.productname}'

    def save(self, *args, **kwargs):
        self.final_price = self.discount_price if self.discount_price > 0 else self.price
        self.total_price = (self.qty) * Decimal(self.final_price)

        # self.final_base = self.discount_base if self.discount_base > 0 else self.base
        # self.total_base = Decimal(self.addlconsole) * Decimal(self.final_base)

        # self.base = (self.base * self.addlconsole)

        super().save(*args, **kwargs)
        self.sizingorder.save()

    def tag_final_price(self):
        return f'{self.final_price}'

    def tag_discount(self):
        return f'{self.discount_price}'

    def tag_price(self):
        return f'{self.price} '

    def tag_final_base(self):
        return f'{self.final_base}'

    def tag_discount_base(self):
        return f'{self.discount_base}'

    def tag_base(self):
        return f'{self.base}'

    # def tag_productcomplexitybase(self):
    #     return f'{(self.productcomplexitybase) * Decimal(self.addlconsole) }'
