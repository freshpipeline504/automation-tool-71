import logging
from typing import Dict, Any, Optional

class AutomationHandler:
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def process_request(self, data: Optional[Dict[str, Any]]) -> bool:
        if not data:
            self.logger.warning("received empty request data")
            return False
        
        try:
            return self._execute_task(data)
        except Exception as e:
            self.logger.error(f"execution failure: {str(e)}")
            return False

    def _execute_task(self, data: Dict[str, Any]) -> bool:
        task_id = data.get("id")
        payload = data.get("payload", {})
        
        self.logger.info(f"processing task {task_id}")
        return bool(payload)

def create_handler(config: Dict[str, Any]) -> AutomationHandler:
    return AutomationHandler(config)