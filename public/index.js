const root = document.getElementById("root");

// CONFIGURAÇÃO DA API - Para Vercel
const API_BASE_URL = "/api";  // Vercel usa rotas relativas

root.innerHTML = `
  <div class="min-h-screen flex items-center justify-center p-4">
    <!-- Header flutuante -->
    <div class="absolute top-4 left-1/2 transform -translate-x-1/2 floating-animation">
      <div class="bg-white bg-opacity-20 backdrop-blur-lg rounded-full px-6 py-2 text-white font-medium">
        <i class="fas fa-clipboard-list mr-2"></i>Pesquisa do Impacto Ambiental 
      </div>
    </div>
    
    <!-- Container principal -->
    <div class="w-full max-w-4xl mt-16">
      <!-- Card principal -->
      <div class="bg-white bg-opacity-10 backdrop-blur-lg card-shadow rounded-3xl p-8 border border-white border-opacity-20">
        <!-- Título -->
        <div class="text-center mb-8">
          <div class="inline-flex items-center justify-center w-20 h-20 bg-blue-500 bg-opacity-20 rounded-full mb-4 floating-animation">
            <i class="fas fa-clipboard-list text-3xl text-white"></i>
          </div>
          <h1 class="text-4xl font-bold text-white mb-2">Vamos Medir as Emissões de Efeito do Evento? </h1>
          <p class="text-white text-opacity-80">O propósito do questionário é coletar informações sobre o deslocamento para a Semana Acadêmica dos Cursos Técnicos da Univates. Os dados serão utilizados para análise do impacto ambiental dos transportes utilizados.</p>
        </div>
        
        <!-- Formulário -->
        <form id="form" class="space-y-8">
          <!-- Seção 1: Dados Pessoais -->
          <div class="bg-white bg-opacity-5 rounded-2xl p-6 border border-white border-opacity-10">
            <h3 class="text-white font-semibold text-xl mb-6 flex items-center">
              <i class="fas fa-user mr-3 text-blue-300"></i>
              Dados Pessoais
            </h3>
            
            <!-- Matrícula -->
            <div class="space-y-2 mb-6">
              <label class="flex items-center text-white font-medium">
                <i class="fas fa-id-card mr-3 text-green-300"></i>
                Digite sua matrícula na Univates (somente números): *
              </label>
              <input 
                type="text" 
                name="matricula" 
                required 
                placeholder="Ex: 123456"
                class="w-full bg-white bg-opacity-20 backdrop-blur-lg border border-white border-opacity-30 px-4 py-3 rounded-xl text-white placeholder-white placeholder-opacity-60 input-focus transition-all duration-300"
              />
            </div>
          </div>

          <!-- Seção 2: Endereços -->
          <div class="bg-white bg-opacity-5 rounded-2xl p-6 border border-white border-opacity-10">
            <h3 class="text-white font-semibold text-xl mb-6 flex items-center">
              <i class="fas fa-map-marker-alt mr-3 text-red-300"></i>
              Endereços de Origem e Destino
            </h3>
            
            <!-- Endereço de Origem -->
            <div class="space-y-2 mb-6">
              <label class="flex items-center text-white font-medium">
                <i class="fas fa-home mr-3 text-green-300"></i>
                Qual seu endereço de origem (rua, número e município)? *
              </label>
              <textarea 
                name="endereco_origem" 
                required 
                rows="3"
                placeholder="Ex: Rua das Flores, 123, Lajeado - RS"
                class="w-full bg-white bg-opacity-20 backdrop-blur-lg border border-white border-opacity-30 px-4 py-3 rounded-xl text-white placeholder-white placeholder-opacity-60 input-focus transition-all duration-300 resize-none"
              ></textarea>
              <p class="text-white text-opacity-60 text-sm">Para garantir a precisão do cálculo de emissões é necessário que seja informado o endereço no padrão solicitado.</p>
            </div>

            <!-- Endereço de Destino -->
            <div class="space-y-2 mb-6">
              <label class="flex items-center text-white font-medium">
                <i class="fas fa-university mr-3 text-blue-300"></i>
                Endereço de destino (Univates):
              </label>
              <input 
                type="text" 
                name="endereco_destino" 
                value="Av. Avelino Talini, 171, Lajeado - RS"
                readonly
                class="w-full bg-white bg-opacity-10 backdrop-blur-lg border border-white border-opacity-20 px-4 py-3 rounded-xl text-white opacity-75"
              />
            </div>

            <!-- Distância -->
            <div class="space-y-2">
              <label class="flex items-center text-white font-medium">
                <i class="fas fa-route mr-3 text-purple-300"></i>
                Distância percorrida (km): *
              </label>
              <div class="relative">
                <input 
                  type="number" 
                  step="0.1" 
                  name="distancia" 
                  required 
                  placeholder="Ex: 15.5"
                  class="w-full bg-white bg-opacity-20 backdrop-blur-lg border border-white border-opacity-30 px-4 py-3 rounded-xl text-white placeholder-white placeholder-opacity-60 input-focus transition-all duration-300"
                />
                <span class="absolute right-4 top-1/2 transform -translate-y-1/2 text-white text-opacity-60 font-medium">km</span>
              </div>
            </div>
          </div>

          <!-- Seção 3: Meio de Transporte -->
          <div class="bg-white bg-opacity-5 rounded-2xl p-6 border border-white border-opacity-10">
            <h3 class="text-white font-semibold text-xl mb-6 flex items-center">
              <i class="fas fa-car mr-3 text-yellow-300"></i>
              Meio de Transporte
            </h3>
            
            <div class="space-y-2 mb-6">
              <label class="text-white font-medium mb-4 block">
                Qual o principal meio de transporte utilizado para o deslocamento até o evento? *
              </label>
              <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="meio_transporte" value="veiculo_proprio" required class="text-green-500">
                  <i class="fas fa-car text-blue-300"></i>
                  <span class="text-white">Veículo próprio</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="meio_transporte" value="carro_aplicativo" required class="text-green-500">
                  <i class="fas fa-taxi text-yellow-300"></i>
                  <span class="text-white">Carro de aplicativo/Táxi</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="meio_transporte" value="motocicleta" required class="text-green-500">
                  <i class="fas fa-motorcycle text-orange-300"></i>
                  <span class="text-white">Motocicleta</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="meio_transporte" value="onibus" required class="text-green-500">
                  <i class="fas fa-bus text-green-300"></i>
                  <span class="text-white">Ônibus</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="meio_transporte" value="bicicleta" required class="text-green-500">
                  <i class="fas fa-bicycle text-green-400"></i>
                  <span class="text-white">Bicicleta</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="meio_transporte" value="caminhando" required class="text-green-500">
                  <i class="fas fa-walking text-green-400"></i>
                  <span class="text-white">Caminhando</span>
                </label>
              </div>
            </div>
          </div>

          <!-- Seção 4: Combustível -->
          <div id="secao-combustivel" class="bg-white bg-opacity-5 rounded-2xl p-6 border border-white border-opacity-10 hidden">
            <h3 class="text-white font-semibold text-xl mb-6 flex items-center">
              <i class="fas fa-gas-pump mr-3 text-red-300"></i>
              Tipo de Combustível
            </h3>
            
            <div class="space-y-2">
              <label class="text-white font-medium mb-4 block">
                Se você selecionou veículo próprio ou motocicleta na pergunta anterior, responda qual o combustível utilizado? *
              </label>
              <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="combustivel" value="gasolina" class="text-green-500">
                  <i class="fas fa-tint text-red-300"></i>
                  <span class="text-white">Gasolina</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="combustivel" value="etanol" class="text-green-500">
                  <i class="fas fa-leaf text-green-300"></i>
                  <span class="text-white">Etanol</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="combustivel" value="diesel" class="text-green-500">
                  <i class="fas fa-truck text-gray-300"></i>
                  <span class="text-white">Diesel</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="combustivel" value="gnv" class="text-green-500">
                  <i class="fas fa-cloud text-blue-300"></i>
                  <span class="text-white">GNV</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="combustivel" value="eletrico" class="text-green-500">
                  <i class="fas fa-bolt text-yellow-300"></i>
                  <span class="text-white">Elétrico</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="combustivel" value="nao_se_aplica" class="text-green-500">
                  <i class="fas fa-times text-gray-300"></i>
                  <span class="text-white">Não se aplica</span>
                </label>
              </div>
            </div>
          </div>

          <!-- Seção 5: Autorização -->
          <div class="bg-white bg-opacity-5 rounded-2xl p-6 border border-white border-opacity-10">
            <h3 class="text-white font-semibold text-xl mb-6 flex items-center">
              <i class="fas fa-shield-alt mr-3 text-green-300"></i>
              Autorização de Dados
            </h3>
            
            <div class="space-y-4">
              <p class="text-white text-opacity-90">
                Autorizo a utilização de meus dados de endereço para o cálculo das emissões de gases de efeito estufa do meu deslocamento da origem até a universidade. *
              </p>
              <div class="flex space-x-6">
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="autorizacao" value="true" required class="text-green-500">
                  <i class="fas fa-check text-green-300"></i>
                  <span class="text-white">Sim</span>
                </label>
                <label class="flex items-center space-x-3 bg-white bg-opacity-10 p-4 rounded-xl cursor-pointer hover:bg-opacity-20 transition-all">
                  <input type="radio" name="autorizacao" value="false" required class="text-green-500">
                  <i class="fas fa-times text-red-300"></i>
                  <span class="text-white">Não</span>
                </label>
              </div>
            </div>
          </div>
          
          <!-- Botão de enviar -->
          <button 
            type="submit" 
            class="w-full bg-gradient-to-r from-green-500 to-blue-600 text-white py-4 rounded-2xl font-bold text-lg btn-hover transition-all duration-300 flex items-center justify-center space-x-3 shadow-lg"
          >
            <i class="fas fa-paper-plane"></i>
            <span>Enviar Dados</span>
            <i class="fas fa-arrow-right"></i>
          </button>
        </form>
        
        <!-- Loading -->
        <div id="loading" class="hidden mt-8 text-center">
          <div class="inline-flex items-center space-x-3 bg-white bg-opacity-20 backdrop-blur-lg px-6 py-3 rounded-full">
            <div class="animate-spin rounded-full h-6 w-6 border-b-2 border-white"></div>
            <span class="text-white font-medium">Enviando dados...</span>
          </div>
        </div>
        
        <!-- Mensagem de Sucesso -->
        <div id="sucesso" class="mt-8 text-center hidden">
          <div class="bg-green-500 bg-opacity-20 backdrop-blur-lg rounded-2xl p-6 border border-green-400 border-opacity-30 result-animation">
            <div class="flex items-center justify-center mb-4">
              <div class="w-16 h-16 bg-green-500 bg-opacity-40 rounded-full flex items-center justify-center">
                <i class="fas fa-check text-3xl text-green-300"></i>
              </div>
            </div>
            <h3 class="text-2xl font-bold text-white mb-3">Dados Enviados com Sucesso!</h3>
            <p class="text-white text-opacity-90 mb-4">
              Obrigado por participar da pesquisa sobre emissão de CO₂. 
              Seus dados foram registrados e contribuirão para nossa análise ambiental.
            </p>
            <div id="registro-info" class="bg-white bg-opacity-10 rounded-xl p-4 mb-4">
              <p class="text-white text-opacity-80 text-sm">
                <i class="fas fa-database mr-2"></i>
                <span id="registro-id"></span>
              </p>
            </div>
            <button 
              onclick="location.reload()" 
              class="bg-white bg-opacity-20 hover:bg-opacity-30 text-white px-6 py-3 rounded-xl transition-all duration-300 font-medium"
            >
              <i class="fas fa-plus mr-2"></i>
              Enviar Novo Formulário
            </button>
          </div>
        </div>
      </div>
      
      <!-- Footer -->
      <div class="text-center mt-8">
        <p class="text-white text-opacity-60">
          <i class="fas fa-university text-blue-400 mr-1"></i>
          Universidade do Vale do Taquari - Univates
        </p>
      </div>
    </div>
  </div>
`;

// Lógica para mostrar/ocultar seção de combustível
document.addEventListener('change', function(e) {
  if (e.target.name === 'meio_transporte') {
    const secaoCombustivel = document.getElementById('secao-combustivel');
    const combustivelInputs = document.querySelectorAll('input[name="combustivel"]');
    
    // Limpar seleção anterior
    combustivelInputs.forEach(input => input.checked = false);
    
    if (['veiculo_proprio', 'carro_aplicativo', 'motocicleta'].includes(e.target.value)) {
      secaoCombustivel.classList.remove('hidden');
      // Tornar combustível obrigatório
      combustivelInputs.forEach(input => input.required = true);
    } else {
      secaoCombustivel.classList.add('hidden');
      // Remover obrigatoriedade e selecionar "não se aplica"
      combustivelInputs.forEach(input => {
        input.required = false;
        if (input.value === 'nao_se_aplica') {
          input.checked = true;
        }
      });
    }
  }
});

document.getElementById("form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const form = e.target;
  const formData = new FormData(form);
  
  // Coletar dados do formulário
  const dados = {
    matricula: formData.get('matricula'),
    endereco_origem: formData.get('endereco_origem'),
    endereco_destino: formData.get('endereco_destino'),
    distancia: parseFloat(formData.get('distancia')),
    meio_transporte: formData.get('meio_transporte'),
    combustivel: formData.get('combustivel') || 'nao_se_aplica',
    autorizacao: formData.get('autorizacao') === 'true'
  };
  
  // Validações no frontend
  if (!dados.matricula || dados.matricula.length < 3) {
    alert('Por favor, digite uma matrícula válida (mínimo 3 caracteres).');
    return;
  }
  
  if (!dados.endereco_origem || dados.endereco_origem.trim().length < 10) {
    alert('Por favor, forneça um endereço de origem mais detalhado.');
    return;
  }
  
  if (!dados.distancia || dados.distancia <= 0) {
    alert('Por favor, digite uma distância válida maior que zero.');
    return;
  }
  
  if (!dados.meio_transporte) {
    alert('Por favor, selecione um meio de transporte.');
    return;
  }
  
  if (!dados.autorizacao) {
    alert('É necessário autorizar o uso dos dados para prosseguir.');
    return;
  }
  
  // Mostrar loading
  document.getElementById("loading").classList.remove("hidden");
  document.getElementById("sucesso").classList.add("hidden");
  
  try {
    const res = await fetch(`${API_BASE_URL}/salvar-dados`, {
      method: "POST",
      headers: { 
        "Content-Type": "application/json"
      },
      body: JSON.stringify(dados),
    });

    const data = await res.json();
    
    if (!res.ok) {
      throw new Error(data.error || 'Erro no servidor');
    }
    
    // Simular um pequeno delay para mostrar o loading
    setTimeout(() => {
      document.getElementById("loading").classList.add("hidden");
      document.getElementById("sucesso").classList.remove("hidden");
      
      // Mostrar informações do registro
      const registroId = document.getElementById("registro-id");
      registroId.textContent = `Registro salvo com ID: ${data.registro_id}`;
      
      // Limpar o formulário
      form.reset();
      
      // Ocultar seção de combustível se estava visível
      document.getElementById("secao-combustivel").classList.add("hidden");
      
    }, 1000);
    
  } catch (error) {
    document.getElementById("loading").classList.add("hidden");
    alert(`Erro: ${error.message}`);
  }
});