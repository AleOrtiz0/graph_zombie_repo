import networkx as nx
from typing import Dict, List, Literal

from public.lib.interfaces import CityGraph, ProxyData, PolicyResult
from public.student_code.convert_to_df import convert_edge_data_to_df, convert_node_data_to_df

class EvacuationPolicy:
    """
    Tu implementación de la política de evacuación.
    Esta es la clase que necesitas implementar para resolver el problema de evacuación.
    """
    
    def __init__(self):
        """Inicializa tu política de evacuación"""
        self.policy_type = "policy_1"  # Política por defecto
        
    def set_policy(self, policy_type: Literal["policy_1", "policy_2", "policy_3", "policy_4"]):
        """
        Selecciona la política a utilizar
        Args:
            policy_type: Tipo de política a utilizar
                - "policy_1": Política básica sin uso de proxies
                - "policy_2": Política usando proxies y sus descripciones
                - "policy_3": Política usando datos de simulaciones previas
                - "policy_4": Política personalizada
        """
        self.policy_type = policy_type
    
    def plan_evacuation(self, city: CityGraph, proxy_data: ProxyData, 
                       max_resources: int) -> PolicyResult:
        """
        Planifica la ruta de evacuación y la asignación de recursos.
        
        Args:
            city: El layout de la ciudad
                 - city.graph: Grafo NetworkX con el layout de la ciudad
                 - city.starting_node: Tu posición inicial
                 - city.extraction_nodes: Lista de puntos de extracción posibles
                 
            proxy_data: Información sobre el ambiente
                 - proxy_data.node_data[node_id]: Dict con indicadores de nodos
                 - proxy_data.edge_data[(node1,node2)]: Dict con indicadores de aristas
                 
            max_resources: Máximo total de recursos que puedes asignar
            
        Returns:
            PolicyResult con:
            - path: List[int] - Lista de IDs de nodos formando tu ruta de evacuación
            - resources: Dict[str, int] - Cuántos recursos de cada tipo llevar:
                       {'explosives': x, 'ammo': y, 'radiation_suits': z}
                       donde x + y + z <= max_resources
        """
        # print(f'City graph: {city.graph} \n')
        # print(f'City starting_node: {city.starting_node}\n')
        # print(f'City extraction_nodes: {city.extraction_nodes}\n')
        # print(f'Proxy node_data: {proxy_data.node_data} \n \n')
        # print(f'Proxy edge_data: {proxy_data.edge_data} \n \n')
        # print(f'Max Resources: {max_resources} \n \n')
        
        
        self.policy_type = "policy_1" # TODO: Cambiar a "policy_2" para probar la política 2, y asi sucesivamente
        
        if self.policy_type == "policy_1":
            return self._policy_1(city, max_resources)
        elif self.policy_type == "policy_2":
            return self._policy_2(city, proxy_data, max_resources)
        elif self.policy_type == "policy_3":
            return self._policy_3(city, proxy_data, max_resources)
        else:  # policy_4
            return self._policy_4(city, proxy_data, max_resources)
    
    def _policy_1(self, city: CityGraph, max_resources: int) -> PolicyResult:
        """
        Política 1: Estrategia básica sin uso de proxies.
        Solo utiliza información básica de nodos y aristas para tomar decisiones.
        
        Esta política debe:
        - NO utilizar los proxies
        - Solo usar información básica del grafo (nodos, aristas, pesos)
        - Implementar una estrategia válida para cualquier ciudad
        """
        # TODO: Implementa tu solución aquí
        target = city.extraction_nodes[0]
        
        try:
            path = nx.shortest_path(city.graph, city.starting_node, target, 
                                  weight='weight')
        except nx.NetworkXNoPath:
            path = [city.starting_node]
            
        resources = {
            'explosives': max_resources // 3,
            'ammo': max_resources // 3,
            'radiation_suits': max_resources // 3
        }
        
        return PolicyResult(path, resources)
    
    def _policy_2(self, city: CityGraph, proxy_data: ProxyData, max_resources: int) -> PolicyResult:
        """
        Política 2: Estrategia usando proxies y sus descripciones.
        Utiliza la información de los proxies basándose en sus descripciones documentadas.
        
        Esta política debe:
        - Utilizar los proxies según sus descripciones en docs/05_guia_proxy.md
        - NO utilizar datos de simulaciones
        - Implementar decisiones basadas en la interpretación de los rangos documentados
        """
        # TODO: Implementa tu solución aquí
        proxy_data_nodes_df = convert_node_data_to_df(proxy_data.node_data)
        proxy_data_edges_df = convert_edge_data_to_df(proxy_data.edge_data)
        
        #print(f'\n Node Data: \n {proxy_data_nodes_df}')
        #print(f'\n Edge Data: \n {proxy_data_edges_df}')
        
        target = city.extraction_nodes[0]
        
        try:
            path = nx.shortest_path(city.graph, city.starting_node, target, 
                                  weight='weight')
        except nx.NetworkXNoPath:
            path = [city.starting_node]
            
        resources = {
            'explosives': max_resources // 3,
            'ammo': max_resources // 3,
            'radiation_suits': max_resources // 3
        }
        
        return PolicyResult(path, resources)
    
    def _policy_3(self, city: CityGraph, proxy_data: ProxyData, max_resources: int) -> PolicyResult:
        """
        Política 3: Estrategia usando datos de simulaciones previas.
        Utiliza estadísticas básicas de simulaciones anteriores para mejorar la toma de decisiones.
        
        Esta política debe:
        - Utilizar datos de simulaciones previas
        - Implementar mejoras basadas en estadísticas básicas
        - NO usar modelos de machine learning
        """
        # TODO: Implementa tu solución aquí
        # Aquí deberías cargar y analizar datos de simulaciones previas
        
        target = city.extraction_nodes[0]
        
        try:
            path = nx.shortest_path(city.graph, city.starting_node, target, 
                                  weight='weight')
        except nx.NetworkXNoPath:
            path = [city.starting_node]
            
        resources = {
            'explosives': max_resources // 3,
            'ammo': max_resources // 3,
            'radiation_suits': max_resources // 3
        }
        
        return PolicyResult(path, resources)
    
    def _policy_4(self, city: CityGraph, proxy_data: ProxyData, max_resources: int) -> PolicyResult:
        """
        Política 4: Estrategia personalizada.
        Implementa tu mejor estrategia usando cualquier recurso disponible.
        
        Esta política puede:
        - Usar cualquier técnica o recurso que consideres apropiado
        - Implementar estrategias avanzadas de tu elección
        """
        # TODO: Implementa tu solución aquí
        proxy_data_nodes_df = convert_node_data_to_df(proxy_data.node_data)
        proxy_data_edges_df = convert_edge_data_to_df(proxy_data.edge_data)
        
        #print(f'\n Node Data: \n {proxy_data_nodes_df}')
        #print(f'\n Edge Data: \n {proxy_data_edges_df}')
        
        target = city.extraction_nodes[0]
        
        try:
            path = nx.shortest_path(city.graph, city.starting_node, target, 
                                  weight='weight')
        except nx.NetworkXNoPath:
            path = [city.starting_node]
            
        resources = {
            'explosives': max_resources // 3,
            'ammo': max_resources // 3,
            'radiation_suits': max_resources // 3
        }
        
        return PolicyResult(path, resources)
    
    
    