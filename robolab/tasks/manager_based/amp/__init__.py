import gymnasium as gym
from . import agents

gym.register(
    id="Atom01-AMP",
    entry_point=f"{__name__}.amp_env:AmpEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.atom01_amp_env_cfg:Atom01AmpEnvCfg",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.atom01_amp_agent_cfg:RslRlOnPolicyRunnerAmpCfg",
    },
)

gym.register(
    id="Atom01-AMP-Play",
    entry_point=f"{__name__}.amp_env:AmpEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.atom01_amp_env_cfg:Atom01AmpEnvCfg_PLAY",
        "rsl_rl_cfg_entry_point": f"{agents.__name__}.atom01_amp_agent_cfg:RslRlOnPolicyRunnerAmpCfg",
    },
)