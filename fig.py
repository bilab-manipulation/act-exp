import matplotlib.pyplot as plt

# 데이터 정의
x = [10, 25, 50, 75, 100, 125, 150, 200]
sim_insertion_human_eval = [0, 0.05, 0.15, 0.15, 0.25, 0.15, 0.15, 0.25]
sim_insertion_human_eval_temporal_agg = [0, 0, 0.1, 0.15, 0.15, 0.15, 0.3, 0.35]
sim_transfer_cube_human_eval = [0.05, 0.55, 0.4, 0.3, 0.4, 0.55, 0.3, 0.25]
sim_transfer_cube_human_eval_temporal_agg = [0.1, 0.5, 0.35, 0.2, 0.25, 0.7, 0.55, 0.7]

def multiple_100(origin_list):
    for i in range(len(origin_list)):
        origin_list[i] = int(origin_list[i] * 100)

multiple_100(sim_insertion_human_eval)
multiple_100(sim_insertion_human_eval_temporal_agg)
multiple_100(sim_transfer_cube_human_eval)
multiple_100(sim_transfer_cube_human_eval_temporal_agg)

    

# 그래프 그리기
plt.plot(x, sim_insertion_human_eval, label='sim_insertion_human_eval', color='orange', marker='o')
plt.plot(x, sim_transfer_cube_human_eval, label='sim_transfer_cube_human_eval', color='green', marker='o')
plt.plot(x, sim_insertion_human_eval_temporal_agg, label='sim_insertion_human_eval_temporal_agg', color='orange', marker='*', linestyle='--')
plt.plot(x, sim_transfer_cube_human_eval_temporal_agg, label='sim_transfer_cube_human_eval_temporal_agg', color='green', marker='*', linestyle='--')

# 그래프 제목 및 축 레이블
plt.title('')
plt.xlabel('Size of action chunk (steps)')
plt.ylabel('Success rate (%)')

# 커스텀 x축 눈금
#custom_ticks = [1, 2, 3, 4, 5, 6, 7, 8]
#custom_labels = ['10', '25', '50', '75', '100', '125', '150', '200']
#plt.xticks(custom_ticks, custom_labels)

# 범례 및 그리드
plt.legend()
#plt.grid(True)
plt.ylim([0, 100])

# 그래프 출력
plt.savefig('fig.png')
#plt.savefig('sim_insertion_human_eval.png')
#plt.savefig('sim_transfer_cube_human_eval.png')
#plt.savefig('sim_insertion_human_eval_temporal_agg.png')
#plt.savefig('sim_transfer_cube_human_eval_temporal_agg.png')