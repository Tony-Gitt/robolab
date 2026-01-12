from dataclasses import MISSING

from isaaclab.utils import configclass

from isaaclab.envs import ManagerBasedRLEnvCfg


@configclass
class AnimationEnvCfg(ManagerBasedRLEnvCfg):
    """Configuration for an animation environment with the manager-based workflow."""
    
    motion_data: object = MISSING
    """Motion data configuration for the animation environment.
    
    Please refer to the :class:`robolab.tasks.manager_based.amp.managers.MotionDataManager` class for more details.
    """

    animation: object = MISSING
    """Animation configuration for the animation environment.
    
    Please refer to the :class:`robolab.tasks.manager_based.amp.managers.AnimationManager` class for more details.
    """