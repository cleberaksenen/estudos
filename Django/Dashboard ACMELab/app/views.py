from django.shortcuts import render, redirect
#from django.http import HttpResponse
from app.models import SC2
from app.forms import Amostramodelform, FilterForm
#from app.forms import Amostramodelform, FilterForm, QualityForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Count, Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px


#------------------   
#Views básicas
class HomePageView(View):
    def get(self, request):
        return render(request, 'home.html')
    
class LaboratorioPageView(View):
    def get(self, request):
        return render(request, 'laboratorio.html')

#------------------   
#Cadastro e visualização de amostras
#@method_decorator(login_required(login_url='login'), name='dispatch')
class Amostras(View):
    def get(self, request):
        search = request.GET.get('search', '').strip()
        
        if search.isdigit():  # Verifica se a busca é numérica
            amostras = SC2.objects.filter(lote=search).order_by('id')
        else:
            amostras = SC2.objects.filter(codigo_interno__icontains=search).order_by('id')

        return render(request, 'amostras.html', {'amostras': amostras})

class New_amostra(CreateView):
    model = SC2
    form_class = Amostramodelform
    template_name = 'cadastro.html'
    success_url = reverse_lazy('amostras_list')

class Detail_amostra(DetailView):
    model = SC2
    template_name = 'amostras_detalhes.html'

class Update_amostra(UpdateView):
    model = SC2
    form_class = Amostramodelform
    template_name = 'amostras_update.html'
    success_url = reverse_lazy('amostras_list')

class Delete_amostra(DeleteView):
    model = SC2
    template_name = 'amostras_delete.html'
    success_url = reverse_lazy('amostras_list')


#------------------   
#Dashboard
#@method_decorator(login_required, name='dispatch')
class SC2BarChartView(View):
    def get(self, request):
        cores_laboratorios = {
            "Hemoce": "#FF5733",        # Laranja vibrante
            "Unadig": "#33FF57",        # Verde neon
            "Lacen": "#5733FF",         # Roxo neon
            "Argos": "#FF33A6",         # Rosa neon
            "HAUW": "#33FFF5",          # Ciano claro
            "Fiocruz CE": "#FFD700",    # Amarelo ouro
            "UF de Sao Joao Del-Rei": "#FF8C00"  # Laranja escuro
        }
        cores_melhor_repeticao = {"Melhor repetição": "#3bd6c6", "Pior repetição": "#ff084a", 
                                  "Controle (NTC)": "#ea00d9"}
        
        cores_qualidade = {"Good": "#00ff9f", "Mediocre": "#feff6e", "Bad": "#cb0c59"}

        cores_resultado = {"Conclusivo": "#05ffa1", "Inconclusivo": "#ff00c1", "Controle (NTC)": "#9600ff", "Em revisão": "#4900ff"}

        cores_variantes = {
                "Inconclusivo": "#740001",
                "Outras": "#8b9dc3",                          # Azul claro
                "VOI Zeta (P.2-like)": "#d3a625",             # Amarelo dourado
                "VOC Gamma (P.1-like)": "#005b96",            # Azul escuro
                "VOC Delta (B.1.617.2-like)": "#008080",      # Verde azulado
                "VOC Omicron (BA.1-like)": "#d896ff",         # Lilás
                "VOC Omicron (BA.2-like)": "#be29ec",         # Roxo
                "VOC Omicron (BA.4-like)": "#FF4500",         # Laranja avermelhado
                "VOC Omicron (BA.5-like)": "#00FF00",         # Verde neon
                "VOC Omicron (BA.5-outras)": "#FF1493",       # Rosa choque
                "VOC Omicron (Recombinante)": "#00CED1"       # Turquesa
            }

        form = FilterForm(request.GET or None)

        selected_lab = request.GET.get('laboratorio_name')
        selected_rep = request.GET.get('melhor_repeticao_name')
        
        def valores():
            total = SC2.objects.count()  # Conta o número total de registros na tabela SC2
            return total
        
        def valores_unicos_conclusivos():
            total_unicos_conclusivos = SC2.objects.filter(
                ~Q(variante__name='Inconclusivo'),
                melhor_repeticao__name='Melhor repetição'
            ).count()
            return total_unicos_conclusivos
        
        def valores_unicos_inconclusivos():
            total_unicos_inconclusivos = SC2.objects.filter(
                Q(variante__name='Inconclusivo'),
                melhor_repeticao__name='Melhor repetição'
            ).count()
            return total_unicos_inconclusivos
        
        def dados_melhor_rep():
            melhor_rep = SC2.objects.filter(melhor_repeticao__name='Melhor repetição').count()
            return melhor_rep
        
        def dados_pior_rep():
            pior_rep = SC2.objects.filter(melhor_repeticao__name='Pior repetição').count()
            return pior_rep
        
        def dados_controles():
            controles = SC2.objects.filter(melhor_repeticao__name='Controle (NTC)').count()
            return controles
        
        def dados_hemoce():
            hemoce = SC2.objects.filter(laboratorio__name='Hemoce').count()
            return hemoce
        
        def dados_unadig():
            unadig = SC2.objects.filter(laboratorio__name='Unadig').count()
            return unadig
        
        def dados_lacen():
            lacen = SC2.objects.filter(laboratorio__name='Lacen').count()
            return lacen
        

        def create_bar_chart(data, group_by, title, color_map, height=300):
            df = pd.DataFrame(data)
            df_grouped = df.groupby([group_by, 'lote']).size().reset_index(name='count')
            
            fig = px.bar(df_grouped, x='lote', y='count', title=title,
                        color=group_by, color_discrete_map=color_map)
            
            fig.update_layout(
                showlegend=False,
                paper_bgcolor='black',
                plot_bgcolor='black',
                font=dict(color='cyan'),
                xaxis=dict(title='Lote', color='cyan', gridcolor='gray'),
                yaxis=dict(title='Quantitativo', color='cyan', gridcolor='gray'),
                margin=dict(l=40, r=40, t=40, b=40),
                height=height)
            
            return fig.to_html(full_html=False)
        
        def calculate_total_counts(data, group_by):
            df = pd.DataFrame(data)
            df_totals = df.groupby(group_by).size().reset_index(name='total_count')           
            totals_dict = df_totals.set_index(group_by).to_dict()['total_count']

            return totals_dict

        # Laboratórios
        if selected_lab:
            data_labs = SC2.objects.filter(laboratorio__name=selected_lab).values('laboratorio__name', 'lote')
        else:
            data_labs = SC2.objects.all().values('laboratorio__name', 'lote')

        chart_html_labs = create_bar_chart(data_labs, 'laboratorio__name', 'Gráfico de Laboratórios', cores_laboratorios)

        labs_dict = calculate_total_counts(data_labs, 'laboratorio__name')
        labs_text = ', '.join([f"{lab}: {count}" for lab, count in labs_dict.items()])

        # Repetições
        if selected_rep:
            data_reps = SC2.objects.filter(melhor_repeticao__name=selected_rep).values('melhor_repeticao__name', 'lote')
        else:
            data_reps = SC2.objects.all().values('melhor_repeticao__name', 'lote')
            
        chart_html_reps = create_bar_chart(data_reps, 'melhor_repeticao__name', 'Gráfico de Repetições', cores_melhor_repeticao)

        reps_dict = calculate_total_counts(data_reps, 'melhor_repeticao__name')
        reps_text = ', '.join([f"{rep}: {count}" for rep, count in reps_dict.items()])

        #-----------------------
        #Gráficos de qualidade
        #-----------------------

        # Gráfico de Dispersão (Qualidade)
        def create_quality_chart(data, color_map, height=300):
            df_qualidade = pd.DataFrame(data)
        
            fig = px.scatter(df_qualidade, x='profundidade_media', y='cobertura', color='qualidade__name', color_discrete_map=color_map)
            fig.update_layout(
                showlegend=False,
                paper_bgcolor='black',
                plot_bgcolor='black',
                font=dict(color='cyan'),
                xaxis=dict(title='Profundidade média', color='cyan', gridcolor='gray'),
                yaxis=dict(title='Cobertura genômica', color='cyan', gridcolor='gray'),
                margin=dict(l=40, r=40, t=40, b=40),
                height=height)
            
            return fig.to_html(full_html=False)

        selected_qua = request.GET.get('lote_number')
        if selected_qua:
            data_qualidade = SC2.objects.filter(lote=selected_qua).values('profundidade_media', 'cobertura', 'qualidade__name', 'melhor_repeticao__name')
        else:
            data_qualidade = SC2.objects.all().values('profundidade_media', 'cobertura', 'qualidade__name', 'melhor_repeticao__name')

        chart_html_qualidade = create_quality_chart(data_qualidade, cores_qualidade)

        qual_dict = calculate_total_counts(data_qualidade, 'qualidade__name')
        qual_text = ', '.join([f"{qual}: {count}" for qual, count in qual_dict.items()])

        reps2_dict = calculate_total_counts(data_qualidade, 'melhor_repeticao__name')
        reps2_text = ', '.join([f"{rep}: {count}" for rep, count in reps2_dict.items()])


        # Gráfico de Dispersão (controle)
        def create_result_chart(data, color_map):
            df_qualidade = pd.DataFrame(data)
        
            fig = px.scatter(df_qualidade, x='profundidade_media', y='cobertura', color='resultado__name', color_discrete_map=color_map)
            fig.update_layout(
                showlegend=False,
                paper_bgcolor='black',
                plot_bgcolor='black',
                font=dict(color='cyan'),
                xaxis=dict(title='Profundidade média', color='cyan', gridcolor='gray'),
                yaxis=dict(title='Cobertura genômica', color='cyan', gridcolor='gray'),
                margin=dict(l=40, r=40, t=40, b=40))
            
            return fig.to_html(full_html=False)

        selected_qua = request.GET.get('lote_number')
        if selected_qua:
            data_qualidade = SC2.objects.filter(lote=selected_qua).values('profundidade_media', 'cobertura', 'resultado__name')
        else:
            data_qualidade = SC2.objects.all().values('profundidade_media', 'cobertura', 'resultado__name')

        chart_html_resultado = create_result_chart(data_qualidade, cores_resultado)

        resu_dict = calculate_total_counts(data_qualidade, 'resultado__name')
        resu_text = ', '.join([f"{resu}: {count}" for resu, count in resu_dict.items()])

        # Gráfico de Linhagens e variantes
        def create_var_chart(data, color_map):
            df = pd.DataFrame(data)
            #df2 = df[(df['resultado_id'] == 1) & (df['melhor_repeticao_id'] == 1)]
            
            var_nome_map = {
                0: 'Inconclusivo',
                1: 'Outras',
                2: 'VOI Zeta (P.2-like)',
                3: 'VOC Gamma (P.1-like)',
                4: 'VOC Delta (B.1.617.2-like)',
                5: 'VOC Omicron (BA.1-like)',
                6: 'VOC Omicron (BA.2-like)',
                7: "VOC Omicron (BA.4-like)",
                8: "VOC Omicron (BA.5-like)",
                9: "VOC Omicron (BA.5-outras)",
                10: "VOC Omicron (Recombinante)"
            }

            var_filt = df.groupby(['variante_id', 'linhagem']).size().reset_index(name='Quantitativo')
            var_filt['variante_nome'] = var_filt['variante_id'].map(var_nome_map).fillna(var_filt['variante_id'])

            var_filt = var_filt[['variante_nome', 'linhagem', 'Quantitativo']]  # Reordenar as colunas

            fig = px.sunburst(var_filt, path=['variante_nome', 'linhagem'], values='Quantitativo', color='variante_nome', color_discrete_map=color_map)

            fig.update_layout(
                showlegend=False,
                paper_bgcolor='black',
                plot_bgcolor='black',
                font=dict(color='cyan'),
                margin=dict(l=40, r=40, t=40, b=40),
                sunburstcolorway=["white"]
            )

            return fig.to_html(full_html=False)

        selected_qua = request.GET.get('lote_number')
        if selected_qua:
            data_qualidade = SC2.objects.filter(lote=selected_qua).values()
        else:
            data_qualidade = SC2.objects.all().values()
        chart_html_variante = create_var_chart(data_qualidade, cores_variantes)

        # Histograma temporal de Linhagens e variantes
        def create_histvar_chart(data, color_map):
            df = pd.DataFrame(data)
            #df2 = df[(df['resultado_id'] == 1) & (df['melhor_repeticao_id'] == 1)]
            
            var_nome_map = {
                0: 'Inconclusivo',
                1: 'Outras',
                2: 'VOI Zeta (P.2-like)',
                3: 'VOC Gamma (P.1-like)',
                4: 'VOC Delta (B.1.617.2-like)',
                5: 'VOC Omicron (BA.1-like)',
                6: 'VOC Omicron (BA.2-like)',
                7: "VOC Omicron (BA.4-like)",
                8: "VOC Omicron (BA.5-like)",
                9: "VOC Omicron (BA.5-outras)",
                10: "VOC Omicron (Recombinante)"
            }

            var_filt = df.groupby(['variante_id', 'mes_coleta']).size().reset_index(name='Quantitativo')
            var_filt['variante_nome'] = var_filt['variante_id'].map(var_nome_map).fillna(var_filt['variante_id'])

            var_filt = var_filt[['variante_nome', 'mes_coleta', 'Quantitativo']]  # Reordenar as colunas

            fig = px.bar(var_filt, x='mes_coleta', y='Quantitativo', color='variante_nome', title='', color_discrete_map=color_map)
            fig.update_layout(
                showlegend=False,
                paper_bgcolor='black',
                plot_bgcolor='black',
                font=dict(color='cyan'),
                xaxis=dict(title='Período', color='cyan', gridcolor='gray'),
                yaxis=dict(title='Quantitativo de variantes', color='cyan', gridcolor='gray'),
                margin=dict(l=40, r=40, t=40, b=40))

            return fig.to_html(full_html=False)

        selected_qua = request.GET.get('lote_number')
        if selected_qua:
            data_qualidade = SC2.objects.filter(lote=selected_qua).values()
        else:
            data_qualidade = SC2.objects.all().values()
        chart_html_var_hist = create_histvar_chart(data_qualidade, cores_variantes)

        total_linhas = valores()
        total_unicos_conclusivos = valores_unicos_conclusivos()
        total_unicos_inconclusivos = valores_unicos_inconclusivos()
        total_melhor_rep = dados_melhor_rep()
        total_pior_rep = dados_pior_rep()
        total_controles = dados_controles()
        total_hemoce = dados_hemoce()
        total_unadig = dados_unadig()
        total_lacen = dados_lacen()


        return render(request, 'dashboard.html', {
            'chart_html_labs': chart_html_labs,
            'labs_text': labs_text,
            'chart_html_reps': chart_html_reps,
            'reps_text': reps_text,
            'chart_html_qualidade': chart_html_qualidade,
            'qual_text': qual_text,
            'reps2_text': reps2_text,
            'chart_html_resultado': chart_html_resultado,
            'resu_text': resu_text,
            'chart_html_variante': chart_html_variante,
            'chart_html_var_hist': chart_html_var_hist,
            'form': form,
            'total_linhas': total_linhas,
            'total_unicos_conclusivos': total_unicos_conclusivos,
            'total_unicos_inconclusivos': total_unicos_inconclusivos,
            'total_melhor_rep': total_melhor_rep,
            'total_pior_rep': total_pior_rep,
            'total_controles': total_controles,
            'total_hemoce': total_hemoce,
            'total_unadig': total_unadig,
            'total_lacen': total_lacen,
            'qual_text': qual_text,
            'reps2_text': reps2_text
            })

        
