from .models import Reserva, Stand
from .forms import ReservaForm, StandForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages import views


# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "reserva/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_reservas'] = Reserva.objects.count()
        context['total_stands'] = Stand.objects.count()
        return context

class ReservasListView(generic.ListView):
  model = Reserva
  paginate_by=2 
  template_name = "reserva/reserva.html"

class ReservaCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Reserva
  form_class = ReservaForm
  template_name = "reserva/form.html"
  success_url = reverse_lazy("reserva_listar")
  success_message = "Reserva cadastrada com sucesso!"
  def form_invalid(self, form):
    print ("!!!!", form.errors)
    return self.render_to_response(self.get_context_data(form=form))
  
  
class ReservaDeleteView(views.SuccessMessageMixin, generic.DeleteView):
  model = Reserva
  template_name = "reserva/reserva_confirm_delete.html"
  success_url = reverse_lazy("reserva_listar")
  success_message = "Reserva removida com sucesso!"
  
class ReservaUpdateView(views.SuccessMessageMixin, generic.UpdateView):
  model = Reserva
  form_class = ReservaForm
  template_name = "reserva/form.html"
  success_url = reverse_lazy("reserva_listar")
  success_message = "Reserva atualizada com sucesso!"

class ReservasListView(generic.ListView): 
  model = Reserva 
  paginate_by=2 
  template_name = "reserva/reserva.html"


#parte dos stands
class StandListView(generic.ListView):
  model = Stand
  paginate_by=2 
  template_name = "reserva/stand/stands.html"

class StandCreateView(views.SuccessMessageMixin, generic.CreateView):
  model = Stand
  form_class = StandForm
  template_name = "reserva/stand/form.html"
  success_url = reverse_lazy("stand_listar")
  success_message = "Stand cadastrado com sucesso!"
  def form_invalid(self, form):
    print ("!!!!", form.errors)
    return self.render_to_response(self.get_context_data(form=form))
  
  
class StandDeleteView(views.SuccessMessageMixin, generic.DeleteView):
  model = Stand
  success_url = reverse_lazy("stand_listar")
  success_message = "Stand removido com sucesso!"
  
class StandUpdateView(views.SuccessMessageMixin, generic.UpdateView):
  model = Stand
  form_class = StandForm
  template_name = "reserva/stand/form.html"
  success_url = reverse_lazy("stand_listar")
  success_message = "Stand atualizado com sucesso!"


class ReservasListView(generic.ListView): 
     model = Reserva 
     paginate_by=2 
     template_name = "reserva/reserva.html"