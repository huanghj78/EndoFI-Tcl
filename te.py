from pathlib import Path
from typing import Dict, Any
# 导入TimeEval相关的模块
from timeeval import TimeEval, DatasetManager, Algorithm, TrainingType, InputDimensionality
from timeeval.adapters import DockerAdapter
from timeeval.constants import HPI_CLUSTER
from timeeval.params import FixedParameters

# 假设你有一个数据集x，保存在文件x.csv中，每行一个数据点，每个数据点有5个特征
# 你可以使用DatasetManager类来加载数据集x，并指定它的标签和属性
dm = DatasetManager(Path("."), create_if_missing=False)
dm.add_dataset("x", "sample.csv", label_column=2, attribute_columns=[0, 1])

# 定义LOF算法，使用DockerAdapter来调用TimeEval Algorithms仓库中的LOF算法容器
# 指定算法的名称、参数、训练类型和输入维度
lof = Algorithm(
    name="LOF",
    main=DockerAdapter("timeeval-algorithms-lof"),
    data_as_file=True,
    training_type=TrainingType.UNSUPERVISED,
    input_dimensionality=InputDimensionality.UNIVARIATE,
    param_config=FixedParameters(
        {"n_neighbors": 20}
    )
)

# 创建TimeEval对象，指定要评估的数据集和算法
timeeval = TimeEval(dm, ["x"], [lof])

# 执行评估，得到异常检测的结果和评价指标
timeeval.run()
results = timeeval.get_results()

# 打印结果
print(results)
