from django import forms

class FormularioItem(forms.Form):
    title = forms.CharField(
                label='Titulo',
                max_length=50,
                min_length=5
            )

    datail = forms.CharField(
                    label='Detalle',
                    widget=forms.Textarea()
                )

    """ date = forms.DateField(
                    label='vencimiento',
                    input_formats=['%d/%m/%Y']
    ) """



