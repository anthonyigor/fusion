from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Servico, Funcionario, Feature
from .forms import ContatoForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        #verifica se já há dados no contexto e recupera-os se necessário
        context = super(IndexView, self).get_context_data(**kwargs)
        #coloca os dados de serviço no contexto
        context['servicos'] = Servico.objects.all
        #coloca os dados de funcionários no contexto
        context['funcionarios'] = Funcionario.objects.all

        features = Feature.objects.all()

        context['features_Col1'] = features[:len(features)//2]
        context['features_Col2'] = features[len(features)//2:]

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar email.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
