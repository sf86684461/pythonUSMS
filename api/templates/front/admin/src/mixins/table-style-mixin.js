// 表格页面样式混入
export default {
  mounted() {
    // 为所有表格页面添加现代化样式类
    this.applyModernTableStyles();
  },
  methods: {
    applyModernTableStyles() {
      // 等待DOM渲染完成
      this.$nextTick(() => {
        // 为主容器添加现代化样式
        const mainContent = document.querySelector('.main-content');
        if (mainContent) {
          mainContent.classList.add('modern-table-page');
        }

        // 为搜索表单添加现代化样式
        const searchForm = document.querySelector('.center-form-pv');
        if (searchForm) {
          searchForm.classList.add('modern-search-form');
        }

        // 为操作按钮区域添加现代化样式
        const actions = document.querySelector('.actions');
        if (actions) {
          actions.classList.add('modern-actions');
        }

        // 为表格容器添加现代化样式
        const tableContainer = document.querySelector('.table-container');
        if (tableContainer) {
          tableContainer.classList.add('modern-table-container');
        }

        // 为分页组件添加现代化样式
        const pagination = document.querySelector('.el-pagination');
        if (pagination) {
          pagination.classList.add('modern-pagination');
        }

        // 优化表格内的图片显示
        this.optimizeTableImages();
        
        // 优化按钮样式
        this.optimizeTableButtons();
      });
    },

    optimizeTableImages() {
      // 为表格中的图片添加现代化样式
      const tableImages = document.querySelectorAll('.el-table img');
      tableImages.forEach(img => {
        img.style.borderRadius = '6px';
        img.style.transition = 'transform 0.3s ease';
        img.addEventListener('mouseenter', () => {
          img.style.transform = 'scale(1.05)';
        });
        img.addEventListener('mouseleave', () => {
          img.style.transform = 'scale(1)';
        });
      });
    },

    optimizeTableButtons() {
      // 为表格中的按钮添加现代化样式
      const tableButtons = document.querySelectorAll('.el-table .el-button');
      tableButtons.forEach(button => {
        button.style.borderRadius = '4px';
        button.style.transition = 'all 0.3s ease';
        button.style.fontWeight = '500';
        
        // 根据按钮类型设置不同的样式
        if (button.classList.contains('view')) {
          button.style.background = 'linear-gradient(135deg, #409eff 0%, #3a8ee6 100%)';
          button.style.border = 'none';
          button.style.boxShadow = '0 1px 3px rgba(64, 158, 255, 0.3)';
        } else if (button.classList.contains('edit')) {
          button.style.background = 'linear-gradient(135deg, #67c23a 0%, #5daf34 100%)';
          button.style.border = 'none';
          button.style.boxShadow = '0 1px 3px rgba(103, 194, 58, 0.3)';
        } else if (button.classList.contains('del')) {
          button.style.background = 'linear-gradient(135deg, #f56c6c 0%, #f25c5c 100%)';
          button.style.border = 'none';
          button.style.boxShadow = '0 1px 3px rgba(245, 108, 108, 0.3)';
        }

        // 添加悬停效果
        button.addEventListener('mouseenter', () => {
          button.style.transform = 'translateY(-1px)';
          if (button.classList.contains('view')) {
            button.style.boxShadow = '0 2px 6px rgba(64, 158, 255, 0.4)';
          } else if (button.classList.contains('edit')) {
            button.style.boxShadow = '0 2px 6px rgba(103, 194, 58, 0.4)';
          } else if (button.classList.contains('del')) {
            button.style.boxShadow = '0 2px 6px rgba(245, 108, 108, 0.4)';
          }
        });

        button.addEventListener('mouseleave', () => {
          button.style.transform = 'translateY(0)';
          if (button.classList.contains('view')) {
            button.style.boxShadow = '0 1px 3px rgba(64, 158, 255, 0.3)';
          } else if (button.classList.contains('edit')) {
            button.style.boxShadow = '0 1px 3px rgba(103, 194, 58, 0.3)';
          } else if (button.classList.contains('del')) {
            button.style.boxShadow = '0 1px 3px rgba(245, 108, 108, 0.3)';
          }
        });
      });
    }
  }
}